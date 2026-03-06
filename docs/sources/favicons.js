document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("a.icon.link").forEach(function (a) {
        try {
            var url = new URL(a.href);
            var img = document.createElement("img");
            img.className = "favicon";
            img.src = "https://www.google.com/s2/favicons?sz=16&domain=" +
                      url.hostname;
            img.alt = "";
            img.onerror = function () { this.remove(); };
            a.classList.add("has-favicon");
            a.insertBefore(img, a.firstChild);
        } catch (e) {}
    });
});
