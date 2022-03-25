const loginForm = document.querySelector('#loginForm');
const content = document.querySelector('#content');
const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)

    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr
    }
    fetch(loginEndpoint, options)
    .then(response=>{
        console.log('Response',response);
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData, getProductList)
    })
    .catch(err=> {
        console.log('err', err)
    })
}

function handleAuthData(authData,callback){
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)

    if(callback){
        callback();
    }
}

function writeContent(data){
    if(content){
        content.innerHTML = "<pre>"+JSON.stringify(data,null,4)+"</pre>"
    }
}

function getFetchOptions(method, body){
    return {
        method: method === null ? "GET" : method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}`
        },
        body: body ? body : null
    }
}

function isTokenNotValid(jsonData) {
    if (jsonData.code && jsonData.code === "token_not_valid"){
        alert("Please login again")
        return false
    }
    return true
}


function getProductList(){
    const endpoint = `${baseEndpoint}/product/`

    const options = getFetchOptions()
    fetch(endpoint, options)
    .then(response=> response.json())
    .then(data=> {
        const validData = isTokenNotValid(data)
        if (validData) {
            writeToContainer(data)
        }
    })
    .catch(err=> {
        console.log('err', err)
    })
}
getProductList()