const loginForm = document.querySelector('#loginForm');
const contentContainer = document.querySelector('#content');
const searchForm = document.getElementById('SearchForm')
const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}
if (searchForm) {
    // handle this login form
    searchForm.addEventListener('submit', handleSearch)
}


function handleSearch(event) {
    event.preventDefault()
    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)
    const endpoint = `${baseEndpoint}/search/?${searchParams}`
    const headers = {
        "Content-Type": "application/json",
    }
    const authToken = localStorage.getItem('access') 
    if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`
    }

    const options = {
        method: "GET",
        headers: headers
    }
    
    fetch(endpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(data => {
        const validData = isTokenNotValid(data)
        if (validData && contentContainer){
            contentContainer.innerHTML = ""
            if (data && data.hits) {
                let htmlStr  = ""
                for (let result of data.hits) {
                    htmlStr += "<li>"+ result.title + "</li>"
                }
                contentContainer.innerHTML = htmlStr
                if (data.hits.length === 0) {
                    contentContainer.innerHTML = "<p>No results found</p>"
                }
            } else {
                contentContainer.innerHTML = "<p>No results found</p>"
            }
        }
    })
    .catch(err=> {
        console.log('err', err)
    })
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
    if(contentContainer){
        contentContainer.innerHTML = "<pre>"+JSON.stringify(data,null,4)+"</pre>"
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
        // run a refresh token fetch
        alert("Please login again")
        return false
    }
    return true
}

function validateJWTToken() {
    // fetch
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            token: localStorage.getItem('access')
        })
    }
    fetch(endpoint, options)
    .then(response=>response.json())
    .then(x=> {
        // refresh token
    })
}

function getProductList(){
    const endpoint = `${baseEndpoint}/product/`

    const options = getFetchOptions()
    fetch(endpoint, options)
    .then(response=> response.json())
    .then(data=> {
        const validData = isTokenNotValid(data)
        if (validData) {
            writeContent(data)
        }
    })
    .catch(err=> {
        console.log('err', err)
    })
}
validateJWTToken()
// getProductList()

const searchClient = algoliasearch('431YZOHOIG','20c4c44fadbea6e92db2bcfafab73c49');

const search = instantsearch({
  indexName: 'Search_Product',
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
  }),

  instantsearch.widgets.clearRefinements({
    container: "#clear-refinements"
 }),

  instantsearch.widgets.refinementList({
    container: "#user-list",
    attribute: 'user'
 }),
 instantsearch.widgets.refinementList({
    container: "#public-list",
    attribute: 'public'
}),

  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
        item:  `<div>
            <div>{{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}</div>
            <div>{{#helpers.highlight}}{ "attribute": "description" }{{/helpers.highlight}}</div>
            
            <p>{{ user }}</p><p>\${{ price }}
        
        </div>`
    }
  })
]);

search.start();
