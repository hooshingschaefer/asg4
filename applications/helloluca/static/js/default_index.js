// This is the js for the default/index.html view.

var app = function () {

    var self = {};

    Vue.config.silent = false; // show all warnings

    // Extends an array
    self.extend = function (a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };

    self.get_products_with_query = function () {

        var req = new XMLHttpRequest();
        req.open('get', get_products_url + '?query=' + self.vue.query);
        req.send();
        req.responseType = 'json';
        req.onload = function () {
            self.vue.product_list = req.response.product_list;
        };
    };

    self.get_products = function () {
        var req = new XMLHttpRequest();
        req.open('GET', get_products_url);
        req.send();
        req.responseType = 'json';
        req.onload = function () {
            self.vue.product_list = req.response.product_list;
        };
    };

    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            product_list: [],
            query: "sdfsdfsdF"
        },
        methods: {
            get_products: self.get_products,
            get_products_with_query: self.get_products_with_query,
        }

    });

    self.get_products();
    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function () { APP = app(); });
