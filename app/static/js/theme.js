document.addEventListener("DOMContentLoaded", function () {

    const themeToggle = document.getElementById("theme-toggle");

    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");
    }

    updateThemeIcon();

    if (themeToggle) {

        themeToggle.addEventListener("click", function () {

            document.body.classList.toggle("dark-mode");

            const isDark =
                document.body.classList.contains("dark-mode");

            localStorage.setItem(
                "theme",
                isDark ? "dark" : "light"
            );

            updateThemeIcon();

        });

    }

    function updateThemeIcon() {

        if (!themeToggle) {
            return;
        }

        const icon =
            themeToggle.querySelector("i");

        if (!icon) {
            return;
        }

        const isDark =
            document.body.classList.contains("dark-mode");

        if (isDark) {

            icon.classList.remove("fa-moon");

            icon.classList.add("fa-sun");

            themeToggle.setAttribute(
                "title",
                "الوضع الفاتح"
            );

        } else {

            icon.classList.remove("fa-sun");

            icon.classList.add("fa-moon");

            themeToggle.setAttribute(
                "title",
                "الوضع الليلي"
            );

        }
    }

});