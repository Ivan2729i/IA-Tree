const monthlyData = JSON.parse(
    document.getElementById("monthly-evaluations-data").textContent
);

const statusData = JSON.parse(
    document.getElementById("status-distribution-data").textContent
);

const metrics = JSON.parse(
    document.getElementById("dashboard-metrics-data").textContent
);

const period = JSON.parse(
    document.getElementById("dashboard-period-data").textContent
);


const rootStyles = getComputedStyle(document.documentElement);

const theme = {
    primary: rootStyles.getPropertyValue("--color-primary").trim(),
    secondary: rootStyles.getPropertyValue("--color-secondary").trim(),
    accent: rootStyles.getPropertyValue("--color-accent").trim(),
    success: rootStyles.getPropertyValue("--color-success").trim(),
    danger: rootStyles.getPropertyValue("--color-danger").trim(),
    muted: rootStyles.getPropertyValue("--color-muted").trim(),
    border: rootStyles.getPropertyValue("--color-border").trim()
};


Chart.defaults.font.family = "ui-sans-serif, system-ui, sans-serif";
Chart.defaults.color = theme.muted;


/* ==========================================
   EVALUACIONES POR MES
========================================== */

const monthlyCanvas = document.getElementById("monthlyEvaluationsChart");

if (monthlyCanvas) {
    new Chart(monthlyCanvas, {
        type: "bar",

        data: {
            labels: monthlyData.map(item => item.month),

            datasets: [
                {
                    label: "Análisis",
                    data: monthlyData.map(item => item.total),
                    backgroundColor: theme.accent,
                    borderRadius: 6,
                    maxBarThickness: 42
                }
            ]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            plugins: {
                legend: {
                    display: false
                },

                tooltip: {
                    displayColors: false
                }
            },

            scales: {
                x: {
                    grid: {
                        display: false
                    },

                    border: {
                        display: false
                    }
                },

                y: {
                    beginAtZero: true,

                    ticks: {
                        precision: 0
                    },

                    grid: {
                        color: theme.border
                    },

                    border: {
                        display: false
                    }
                }
            }
        }
    });
}


/* ==========================================
   MEDIDOR DE RESULTADOS
========================================== */

const statusCanvas = document.getElementById("statusChart");

if (statusCanvas) {
    const withoutFindings = statusData.without_findings;
    const withFindings = statusData.with_findings;

    const total = withoutFindings + withFindings;
    const hasData = total > 0;

    const chartData = hasData
        ? [withoutFindings, withFindings]
        : [1];

    const chartColors = hasData
        ? [theme.success, theme.danger]
        : [theme.border];


    new Chart(statusCanvas, {
        type: "doughnut",

        data: {
            labels: hasData
                ? ["Sin hallazgos", "Con hallazgos"]
                : ["Sin datos"],

            datasets: [
                {
                    data: chartData,
                    backgroundColor: chartColors,
                    borderWidth: 0,
                    hoverOffset: hasData ? 4 : 0
                }
            ]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            rotation: -90,
            circumference: 180,
            cutout: "76%",

            plugins: {
                legend: {
                    display: false
                },

                tooltip: {
                    enabled: hasData
                }
            }
        }
    });


    const percentageElement = document.getElementById("statusChartPercentage");
    const textElement = document.getElementById("statusChartText");

    if (hasData) {
        const percentage = Math.round((withoutFindings / total) * 100);

        percentageElement.textContent = `${percentage}%`;
        textElement.textContent = "sin hallazgos";
    }
}


/* ==========================================
   MES ACTUAL VS MES ANTERIOR
========================================== */

const comparisonCanvas = document.getElementById("monthComparisonChart");

if (comparisonCanvas) {
    new Chart(comparisonCanvas, {
        type: "bar",

        data: {
            labels: [
                period.previous_month,
                period.current_month
            ],

            datasets: [
                {
                    label: "Análisis",
                    data: [
                        metrics.previous_month,
                        metrics.current_month
                    ],
                    backgroundColor: [
                        theme.secondary,
                        theme.accent
                    ],
                    borderRadius: 8,
                    maxBarThickness: 90
                }
            ]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            plugins: {
                legend: {
                    display: false
                },

                tooltip: {
                    displayColors: false
                }
            },

            scales: {
                x: {
                    grid: {
                        display: false
                    },

                    border: {
                        display: false
                    }
                },

                y: {
                    beginAtZero: true,

                    ticks: {
                        precision: 0
                    },

                    grid: {
                        color: theme.border
                    },

                    border: {
                        display: false
                    }
                }
            }
        }
    });
}
