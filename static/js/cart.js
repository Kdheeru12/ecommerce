function getCookie(name){
    var cookieArr = document.cookie.split(";");
    for(var i=0;i<cookieArr.length;i++){
        var cookiePair = cookieArr[i].split("=");
        if(name == cookiePair[0].trim()){
            return decodeURIComponent(cookiePair[1])
        }
    }
    return null
}
var cart = JSON.parse(getCookie('cart'))
if(cart == undefined){
    cart = {}
    console.log('cart created')
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
}
console.log('Cart:',cart)
console.log('hello worlds')
var updateBtns = document.getElementsByClassName('update-cart')
function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getToken('csrftoken');
console.log(csrftoken)
for (i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId,'Action:',action)
        if (user == 'AnonymousUser'){
            addCookieItem(productId,action)
        }
        else{
            updateUserOrder(productId,action)
            
        }
    })
}
function addCookieItem(productId,action){
    console.log('sss')
    if (action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity':1}
            console.log('a')
        }
        else{
            cart[productId]['quantity'] += 1
            console.log('v')
        }
    }
    if (action == 'remove'){
        cart[productId]['quantity'] -= 1 
        if(cart[productId]['quantity'] <= 0){
            console.log('remove')
            delete cart[productIds]
        }
    }
    console.log('Cart:',cart)

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}
function updateUserOrder(productId,action){
    console.log('json is workings')
    var url = '/update_item/'
    console.log(url)
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:',data)
        location.reload()
    })      

}