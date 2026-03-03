.. _adsp sc598 clock tree:

SC598 Clock Tree
================

.. mermaid::

   graph LR
       Crystal["SYS_CLKIN0<br/>25 MHz<br/>(sc5xx.dtsi:80)"]

       subgraph CGU0["CGU0 - Main CGU (clk-adi-sc598.c:100-209)"]
           DF0["DF: ÷1<br/>25 MHz"]
           VCO0["VCO: ×80<br/>2000 MHz<br/>(CGU_CTL MSEL)"]
           PLL0["PLLCLK: ÷2<br/>1000 MHz<br/>(line 125-128)"]

           CCLK0_0["CCLK0_0<br/>500 MHz<br/>÷2 (CDIV)"]
           SYSCLK0["SYSCLK_0<br/>250 MHz<br/>÷4 (SYSSEL)"]
           DCLK0["DCLK_0<br/>333 MHz<br/>÷3 (DDIV)"]
           OCLK0["OCLK_0<br/>62.5 MHz<br/>÷16 (ODIV)"]

           SCLK0_0["SCLK0_0<br/>62.5 MHz<br/>÷4"]
           SCLK1_0["SCLK1_0<br/>125 MHz<br/>÷2"]

           CCLK2_0["CCLK2_0<br/>667 MHz<br/>VCO÷3 direct<br/>(line 158-161)"]

           DCLK0_HALF["DCLK_0_HALF<br/>167 MHz<br/>÷2 (line 223)"]
       end

       subgraph CGU1["CGU1 - Secondary CGU (clk-adi-sc598.c:104-220)"]
           DF1["DF: ÷1<br/>25 MHz"]
           VCO1["VCO: ×64<br/>1600 MHz"]
           PLL1["PLLCLK: ÷2<br/>800 MHz"]

           CCLK0_1["CCLK0_1<br/>400 MHz<br/>÷2"]
           SYSCLK1["SYSCLK_1<br/>200 MHz<br/>÷4"]
           DCLK1["DCLK_1<br/>400 MHz<br/>÷2"]
           OCLK1["OCLK_1<br/>50 MHz<br/>÷16"]

           SCLK0_1["SCLK0_1<br/>50 MHz<br/>÷4"]
           SCLK1_1["SCLK1_1<br/>100 MHz<br/>÷2"]

           CCLK2_1["CCLK2_1<br/>533 MHz<br/>VCO÷3 direct"]

           SCLK1_1_HALF["SCLK1_1_HALF<br/>50 MHz<br/>÷2 (line 231)"]
       end

       subgraph PLL3["3rd PLL - Optional DDR Source<br/>(clk-adi-sc598.c:108-111, clkinit.c:383-440)"]
           PLL3_VCO["VCO: ×64<br/>1600 MHz"]
           PLL3_OUT["3PLL_DDIV<br/>400 MHz<br/>÷2"]
           PLL3_DDR_SEL["DDR Mux<br/>(line 285-287)<br/>selects DCLK_0 or 3PLL"]
       end

       subgraph CDU["CDU - Clock Distribution (0x3108F000)"]
           SHARC0["CLKO0: SHARC-FX<br/>500 MHz<br/>(CDU_CFG0)"]
           SHARC1["CLKO1: SHARC1<br/>500 MHz<br/>(CDU_CFG1)"]
           ARM["CLKO2: ARM<br/>533 MHz<br/>(CDU_CFG2)"]
           DDR["CLKO3: DDR<br/>333 MHz<br/>(CDU_CFG3)"]
           CAN["CLKO4: CAN<br/>50 MHz<br/>(CDU_CFG4)"]
           SPDIF["CLKO5: SPDIF<br/>125 MHz<br/>(CDU_CFG5)"]
           SPI["CLKO6: SPI<br/>62.5 MHz<br/>(CDU_CFG6)"]
           GIGE["CLKO7: GigE<br/>62.5 MHz<br/>(CDU_CFG7)"]
           LP["CLKO8: LP<br/>400 MHz<br/>(CDU_CFG8)"]
           LP_DDR["CLKO9: LP_DDR<br/>62.5 MHz<br/>(CDU_CFG9)"]
           OSPI["CLKO10: OSPI<br/>100 MHz<br/>(CDU_CFG10)"]
           TRACE["CLKO12: TRACE<br/>62.5 MHz<br/>(CDU_CFG12)"]
           EMMC["CLKO13: EMMC<br/>167 MHz<br/>(CDU_CFG13)"]
           EMMC_TMR["CLKO14: EMMC_TMR<br/>50 MHz<br/>(CDU_CFG14)"]
       end

       Crystal --> DF0
       Crystal --> DF1
       Crystal --> PLL3_VCO

       DF0 --> VCO0
       VCO0 --> PLL0
       VCO0 --> CCLK2_0

       PLL0 --> CCLK0_0
       PLL0 --> SYSCLK0
       PLL0 --> DCLK0
       PLL0 --> OCLK0

       SYSCLK0 --> SCLK0_0
       SYSCLK0 --> SCLK1_0
       DCLK0 --> DCLK0_HALF

       DF1 --> VCO1
       VCO1 --> PLL1
       VCO1 --> CCLK2_1

       PLL1 --> CCLK0_1
       PLL1 --> SYSCLK1
       PLL1 --> DCLK1
       PLL1 --> OCLK1

       SYSCLK1 --> SCLK0_1
       SYSCLK1 --> SCLK1_1
       SCLK1_1 --> SCLK1_1_HALF

       PLL3_VCO --> PLL3_OUT
       PLL3_OUT --> PLL3_DDR_SEL
       DCLK0 --> PLL3_DDR_SEL

       CCLK0_0 -.-> SHARC0
       CCLK0_0 -.-> SHARC1
       CCLK2_1 -.-> ARM
       PLL3_DDR_SEL -.-> DDR
       OCLK1 -.-> CAN
       SCLK1_0 -.-> SPDIF
       SCLK0_0 -.-> SPI
       SCLK0_0 -.-> GIGE
       CCLK0_1 -.-> LP
       OCLK0 -.-> LP_DDR
       SCLK1_1 -.-> OSPI
       SCLK0_0 -.-> TRACE
       DCLK0_HALF -.-> EMMC
       SCLK1_1_HALF -.-> EMMC_TMR

       classDef cgu0 fill:#e1f5ff,stroke:#01579b,stroke-width:2px
       classDef cgu1 fill:#fff3e0,stroke:#e65100,stroke-width:2px
       classDef pll3 fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
       classDef cdu fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px

       class CCLK0_0,SYSCLK0,DCLK0,OCLK0,SCLK0_0,SCLK1_0,CCLK2_0,DCLK0_HALF cgu0
       class CCLK0_1,SYSCLK1,DCLK1,OCLK1,SCLK0_1,SCLK1_1,CCLK2_1,SCLK1_1_HALF cgu1
       class PLL3_OUT pll3
       class SHARC0,SHARC1,ARM,DDR,CAN,SPDIF,SPI,GIGE,LP,LP_DDR,OSPI,TRACE,EMMC,EMMC_TMR cdu

- **Solid lines**: Clock flow through dividers
- **Dashed lines**: CDU mux selection to peripherals
- **Blue boxes**: CGU0 outputs (Main CGU)
- **Orange boxes**: CGU1 outputs (Secondary CGU)
- **Purple boxes**: 3rd PLL outputs (DDR-specific)
- **Green boxes**: CDU peripheral outputs
