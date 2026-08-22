document.addEventListener("DOMContentLoaded", function () {

    // ============================================
    // Weekend
    // ============================================

    const weekendCheck =
        document.getElementById("weekendCheck");

    const weekendValue =
        document.getElementById("weekendValue");


    if (weekendCheck) {

        weekendCheck.addEventListener(
            "change",
            function () {

                weekendValue.value =
                    this.checked ? "1" : "0";

            }
        );

    }


    // ============================================
    // Exam
    // ============================================

    const examCheck =
        document.getElementById("examCheck");

    const examValue =
        document.getElementById("examValue");


    if (examCheck) {

        examCheck.addEventListener(
            "change",
            function () {

                examValue.value =
                    this.checked ? "1" : "0";

            }
        );

    }


    // ============================================
    // Event
    // ============================================

    const eventCheck =
        document.getElementById("eventCheck");

    const eventValue =
        document.getElementById("eventValue");


    if (eventCheck) {

        eventCheck.addEventListener(
            "change",
            function () {

                eventValue.value =
                    this.checked ? "1" : "0";

            }
        );

    }


    // ============================================
    // Form loading state
    // ============================================

    const form =
        document.getElementById("predictionForm");


    if (form) {

        form.addEventListener(
            "submit",
            function () {

                const button =
                    form.querySelector(
                        ".predict-button"
                    );

                if (button) {

                    button.querySelector(
                        "span:first-child"
                    ).textContent =
                        "Analyzing Network...";

                    button.style.opacity = "0.8";

                }

            }
        );

    }

});