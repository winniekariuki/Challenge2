# ApplicationStore
[![Build Status](https://travis-ci.org/winniekariuki/Challenge2.svg?branch=master)](https://travis-ci.org/winniekariuki/Challenge2)
[![Coverage Status](https://coveralls.io/repos/github/winniekariuki/Challenge2/badge.svg?branch=develop)](https://coveralls.io/github/winniekariuki/Challenge2?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/7208309d388e16f5a084/maintainability)](https://codeclimate.com/github/winniekariuki/Challenge2/maintainability)
https://challeng.herokuapp.com
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.
**Sign up endpoint**
Enables a new user to sign up into the application.
__Router__ used 'api/v1/users' POST METHOD.
**Login endpoint**
Enables a registered user to login into the application after which an access token is assigned to him/her to enable him/her to access authenticated endpoints.
__Router used__'api/v1/login' POST METHOD.
**Post Product endpoint**
Enables the store admin to create a new product and post.Only the store admin can access this endpoint.
_Router used_'api/v1/products' POST METHOD.
**GET product endpoint**
No access token required.The endpoint enables a user to view all the available products in the inventory.
_Router used_'api/vi/products' GET METHOD.
**GET Single product**
No access token required enables a user 

    Sign up to the application
    Login to the application
    Post a product
    Post a Sale
    Get all products
    Get single product
    Get all products
    Get all sales
    Get single sale
