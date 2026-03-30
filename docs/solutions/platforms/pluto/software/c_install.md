# C Installation and Examples

```{image} resources/software.svg
:width: 400px
:align: right
```  

## C
If you prefer to work with C, you can use the `libiio` library to interface with PlutoSDR. The `libiio` library provides a low-level API for controlling Pluto and accessing its data. You can install `libiio` from the Analog Devices website or using your package manager if it is available. Once you have `libiio` installed, you can use the following code to read samples from [PlutoSDR in C](https://analogdevicesinc.github.io/documentation/tools/pluto/transceiver_transferring_data.html#pluto-transceiver-transferring-data):

```{clear-content}
```
```{code-block} c
// main.c
// Pluto (AD9361) RX streaming example using libiio over network.
//
// What it does:
//  1) Connects to Pluto at 192.168.2.1 via iiod
//  2) Configures RX (sample rate, RF bandwidth, gain mode, RX LO freq) via ad9361-phy
//  3) Streams one RX buffer from cf-ad9361-lpc
//  4) Prints first 10 IQ samples (assumes int16 interleaved I,Q)
//
// Build (WSL):
//   gcc -g main.c -o iio_rx $(pkg-config --cflags --libs libiio)
//
// Run:
//   ./iio_rx

#include <iio.h>
#include <stdio.h>
#include <stdint.h>
#include <errno.h>
#include <string.h>


static int write_attr(struct iio_channel *ch, const char *attr, const char *val,
                      const char *ch_name)
{
    int ret = iio_channel_attr_write(ch, attr, val);
    if (ret < 0) {
        // libiio often returns -errno style values
        int e = -ret;
        fprintf(stderr,
                "ERROR: write %s.%s = %s failed, ret=%d (errno=%d: %s)\n",
                ch_name, attr, val, ret, e, strerror(e));
    } else {
        printf("OK: %s.%s = %s\n", ch_name, attr, val);
    }
    return ret;
}

static void panic(const char *msg)
{
    fprintf(stderr, "ERROR: %s\n", msg);
}


int main(void)
{
    int ret = 0;

    // 1) Create a network context (Pluto default IP)
    struct iio_context *ctx = iio_create_context_from_uri("ip:192.168.2.1");
    if (!ctx) {
        panic("Failed to create IIO context (ip:192.168.2.1). Is iiod running / reachable?");
        return 1;
    }

    printf("Context: %s\n", iio_context_get_name(ctx));
    printf("Description: %s\n", iio_context_get_description(ctx));
    printf("Devices: %u\n\n", iio_context_get_devices_count(ctx));

    // 2) Find control device
    struct iio_device *phy = iio_context_find_device(ctx, "ad9361-phy");
    if (!phy) {
        panic("Failed to find device: ad9361-phy");
        ret = 1;
        goto cleanup_ctx;
    }

    // 3) Find the RX control channel on ad9361-phy
    // From your dump: voltage0 (input) exists; voltage1 does NOT.
    struct iio_channel *phy_rx = iio_device_find_channel(phy, "voltage0", false);
    if (!phy_rx) {
        panic("Failed to find RX control channel voltage0 (input) on ad9361-phy");
        ret = 1;
        goto cleanup_ctx;
    }

    // RX LO is altvoltage0 (output) on ad9361-phy
    struct iio_channel *rx_lo = iio_device_find_channel(phy, "altvoltage0", true);
    if (!rx_lo) {
        panic("Failed to find RX LO channel altvoltage0 (output) on ad9361-phy");
        ret = 1;
        goto cleanup_ctx;
    }

    // 4) Configure RX path
    // sample rate
    int rc;

    rc = write_attr(phy_rx, "sampling_frequency", "1000000", "ad9361-phy:voltage0(in)");
    if (rc < 0) goto cleanup_ctx;

    rc = write_attr(phy_rx, "rf_bandwidth", "1000000", "ad9361-phy:voltage0(in)");
    if (rc < 0) goto cleanup_ctx;

    rc = write_attr(phy_rx, "gain_control_mode", "slow_attack", "ad9361-phy:voltage0(in)");
    if (rc < 0) goto cleanup_ctx;

    rc = write_attr(rx_lo, "frequency", "2400000000", "ad9361-phy:altvoltage0(out)");
    if (rc < 0) goto cleanup_ctx;

    // 5) Find RX streaming device
    struct iio_device *rx = iio_context_find_device(ctx, "cf-ad9361-lpc");
    if (!rx) {
        panic("Failed to find RX streaming device cf-ad9361-lpc");
        ret = 1;
        goto cleanup_ctx;
    }

    // 6) Find RX streaming channels (I/Q) on cf-ad9361-lpc
    struct iio_channel *rx_i = iio_device_find_channel(rx, "voltage0", false);
    struct iio_channel *rx_q = iio_device_find_channel(rx, "voltage1", false);
    if (!rx_i || !rx_q) {
        panic("Failed to find RX streaming channels voltage0/voltage1 on cf-ad9361-lpc");
        ret = 1;
        goto cleanup_ctx;
    }

    iio_channel_enable(rx_i);
    iio_channel_enable(rx_q);

    // 7) Create RX buffer
    const size_t samples_per_buffer = 4096;
    struct iio_buffer *buf = iio_device_create_buffer(rx, samples_per_buffer, false);
    if (!buf) {
        panic("Failed to create RX buffer");
        ret = 1;
        goto disable_channels;
    }

    // 8) Refill buffer once
    const ssize_t nbytes = iio_buffer_refill(buf);
    if (nbytes < 0) {
        fprintf(stderr, "ERROR: iio_buffer_refill failed (ret=%zd)\n", nbytes);
        ret = 1;
        goto destroy_buffer;
    }

    // 9) Print first 10 IQ pairs
    const ptrdiff_t step = iio_buffer_step(buf);
    char *p   = (char *)iio_buffer_first(buf, rx_i);
    char *end = (char *)iio_buffer_end(buf);

    printf("Refilled %zd bytes, step=%td bytes\n", nbytes, step);

    int printed = 0;
    for (; p < end && printed < 10; p += step) {
        // Most Pluto streams are interleaved int16: I then Q.
        int16_t i_sample = ((int16_t *)p)[0];
        int16_t q_sample = ((int16_t *)p)[1];
        printf("Sample %d: I=%d  Q=%d\n", printed, i_sample, q_sample);
        printed++;
    }

destroy_buffer:
    iio_buffer_destroy(buf);

disable_channels:
    iio_channel_disable(rx_q);
    iio_channel_disable(rx_i);

cleanup_ctx:
    iio_context_destroy(ctx);
    return ret ? 1 : 0;
}

```

```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```
