function changeColor() {
    // Generate a random number between 0 and 16777215 (which is FFFFFF in hex)
    // 16777215 is the highest color code in hexadecimal for RGB colors
    //toString(16). This converts the random number into a hexadecimal string, like: e3a55f, 4f09c2, ff33aa
    let color = "#" + Math.floor(Math.random() * 16777215).toString(16);

    // Set the body's background color to the random color
    document.body.style.background = color;
}