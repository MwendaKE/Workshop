// ----------------------------
// PRODUCTS DATA
// ----------------------------
const products = [
    {id:1, name:"Smartphone", price:500, img:"https://via.placeholder.com/150"},
    {id:2, name:"Laptop", price:1200, img:"https://via.placeholder.com/150"},
    {id:3, name:"Headphones", price:150, img:"https://via.placeholder.com/150"},
    {id:4, name:"Smartwatch", price:250, img:"https://via.placeholder.com/150"},
    {id:5, name:"Camera", price:800, img:"https://via.placeholder.com/150"},
];

// CART
let cart = [];

// DOM ELEMENTS
const productsDiv = document.getElementById("products");
const cartItemsDiv = document.getElementById("cartItems");
const totalDiv = document.getElementById("total");
const clearCartBtn = document.getElementById("clearCart");
const checkoutBtn = document.getElementById("checkoutBtn");
const modal = document.getElementById("thankYouModal");
const closeModalBtn = document.getElementById("closeModal");

// ----------------------------
// SHOW PRODUCTS
// ----------------------------
function showProducts(){
    productsDiv.innerHTML = "";
    products.forEach(p=>{
        const div = document.createElement("div");
        div.classList.add("product");
        div.innerHTML = `
            <img src="${p.img}" alt="${p.name}">
            <h3>${p.name}</h3>
            <p>Price: $${p.price}</p>
            <button onclick="addToCart(${p.id})">Add to Cart</button>
        `;
        productsDiv.appendChild(div);
    });
}

// ----------------------------
// ADD TO CART
// ----------------------------
function addToCart(id){
    const product = products.find(p=>p.id===id);
    const item = cart.find(c=>c.id===id);

    if(item){
        item.qty++;
    } else {
        cart.push({...product, qty:1});
    }
    showCart();
}

// ----------------------------
// SHOW CART
// ----------------------------
function showCart(){
    cartItemsDiv.innerHTML = "";
    let total = 0;
    cart.forEach(item=>{
        total += item.price * item.qty;
        const div = document.createElement("div");
        div.classList.add("cart-item");
        div.innerHTML = `
            <span>${item.name} ($${item.price})</span>
            <input class="quantity" type="number" value="${item.qty}" min="1" onchange="updateQty(${item.id}, this.value)">
            <button onclick="removeFromCart(${item.id})">Remove</button>
        `;
        cartItemsDiv.appendChild(div);
    });
    totalDiv.textContent = `Total: $${total}`;
}

// ----------------------------
// UPDATE QUANTITY
// ----------------------------
function updateQty(id, qty){
    const item = cart.find(c=>c.id===id);
    item.qty = parseInt(qty);
    showCart();
}

// ----------------------------
// REMOVE FROM CART
// ----------------------------
function removeFromCart(id){
    cart = cart.filter(c=>c.id!==id);
    showCart();
}

// ----------------------------
// CLEAR CART
// ----------------------------
clearCartBtn.addEventListener("click", ()=>{
    cart = [];
    showCart();
});

// ----------------------------
// CHECKOUT
// ----------------------------
checkoutBtn.addEventListener("click", ()=>{
    if(cart.length === 0) return alert("Cart is empty!");
    // Normally, here you'd send cart to server and process payment
    cart = [];
    showCart();
    modal.style.display = "flex"; // show modal
});

// ----------------------------
// CLOSE MODAL
// ----------------------------
closeModalBtn.addEventListener("click", ()=>{
    modal.style.display = "none";
});

// ----------------------------
// INIT
// ----------------------------
showProducts();
showCart();