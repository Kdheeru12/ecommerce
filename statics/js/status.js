console.log('status js')
function getTokens(name) {
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
var csrftoken = getTokens('csrftoken');
console.log(csrftoken)   
var orderBtn = document.getElementsByClassName('order-status')
for (i=0;i<orderBtn.length;i++){
    orderBtn[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId,'Action:',action)
        if (user == 'AnonymousUser'){
            console.log('dddd')
        }
        else{
            orderStatus(productId,action)    
        }
    })

}
function orderStatus(productId,action){
    console.log('hell0')
    var url = '/order_owner'
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