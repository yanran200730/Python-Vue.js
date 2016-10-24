<template>
    <div class="wrap">
        <Hearders></Hearders>
        <router-view></router-view>
    </div>
</template>

<script type="text/babel">
    import Hearders from 'components/Hearders.vue'

    export default {
        components: {
            Hearders
        },
        data: function(){
            return {
                name : "yanran"
            }
        }
    }
</script>

<style>
    body,ol,ul,li,p,h1,h2,h3,h4,h5,h6 {
        margin: 0;
        padding: 0;
    }

    h1,h2,h3,h4,h5,h6 {
        font-size: 0.16rem;
    }

    .clearfix:after {
        content: "."; 
        display: block; 
        height: 0; 
        clear: both; 
        visibility: hidden;  
    }

    .clearfix {
        zoom: 1; 
    }

    body {
        color: #555;
        font-size: 14px;
        font-family: "微软雅黑";
        word-spacing: 0.05em;
        -webkit-tap-highlight-color:transparent;
    }

    a {
        text-decoration: none;
        color: #1B1B1B;
        -webkit-tap-highlight-color:transparent;
        cursor: pointer;
    }

    ul,ol {
        list-style: none;
    }


</style>