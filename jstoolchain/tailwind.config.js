/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["../library/templates/**/*.html"],
    theme: {
        extend: {},
    },
    plugins: [require("daisyui")],
    daisyui: {
        themes: ["forest"]
    },
}

