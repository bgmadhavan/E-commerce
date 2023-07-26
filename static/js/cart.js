var updatebtn=document.getElementsByClassName('update-cart')

for(var i=0;i<updatebtn.length;i++)
{
    updatebtn[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action =this.dataset.action
        console.log(productId,action,user)

        if(user=='AnonymousUser')
        {
            console.log('Not logged in')
        }
        else{
            updateUserOrder(productId,action)
        }


    })
}

function updateUserOrder(productId,action)
{
    console.log('User logged in sending data.....')

    var url='/update_item/'

    fetch(url,{
        method:'POST',
        headers:{
            'content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data',data)
        location.reload()
    })
}



var updatewish=document.getElementsByClassName('updatewish')

for(var i=0;i<updatewish.length;i++)
{
    updatewish[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action =this.dataset.action
        console.log(productId,action,user)

        if(user=='AnonymousUser')
        {
            console.log('Not logged in')
        }
        else{
            updateUserWish(productId,action)
        }


    })
}

function updateUserWish(productId,action)
{
    console.log('User logged in sending data.....')

    var url='/updatewish/'

    fetch(url,{
        method:'POST',
        headers:{
            'content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data',data)
        location.reload()
    })
}