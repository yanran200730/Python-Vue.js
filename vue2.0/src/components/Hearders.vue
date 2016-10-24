<template>
    <div class="header">
        <div class="logo">
            <a href="javascript">
                <img src="../assets/logo.png">
            </a>
            <div class="links">
                <a href="javascript:;">关于ZAKER</a>
                <a href="javascript:;">GitHub</a>
                <a href="javascript:;">个人Blog</a>
            </div>
        </div>
        <nav class="nav">
            <ul class="list">
                <li><a class="active" href="javascript:;">热点</a></li>
                <li><a href="javascript:;">娱乐</a></li>
                <li><a href="javascript:;">体育</a></li>
                <li><a href="javascript:;">科技</a></li>
                <li><a href="javascript:;">互联网</a></li>
                <li><a href="javascript:;">科学</a></li>
                <li><a href="javascript:;">美食</a></li>
                <li><a href="javascript:;">电影</a></li>
                <li><a href="javascript:;">社会</a></li>
                <li><a href="javascript:;">星座</a></li>
            </ul>  
        </nav>
    </div>
</template>
<style scoped>
    html {
        /*overflow: hidden;*/
    }
    
    .logo {
        margin: 0 auto;
        max-width: 1000px;
        height: 100px;
        position: relative;
    }

    .logo > img {
        vertical-align: middle;
    }

    .logo .links {
        position: absolute;
        top: 0;
        right: 0;
        line-height: 100px;
    }

    .links > a {
        display: inline-block;
        margin: 0 15px;
    }

    .nav {
        /*max-width: 100%;*/
        background-color: #F5F5F5;
    }

    .list {
        max-width: 1000px;
        margin: 0 auto;
    }

    .nav {
        font-size: 16px;
    }

    .nav ul {
        height: 60px;
    }

    .nav ul li  {
        font-family: "微软雅黑";
        float: left;
        line-height: 60px;
        display: inline-block;
    }

    .nav ul li a {
        height: 100%;
        display: inline-block;
        padding: 0 25px;
    }

    .nav ul li a:hover {
        color: #FB4747;
        background-color: #DEDEDE;
    }

    .nav ul li a:visited {
        color: #FB4747;
        background-color: #DEDEDE;        
    }

    @media screen and (max-width: 840px){
        .links {
            display: none;
        }

        .logo {
            height: 40px;
            background-color: #f84d4d;
        }

        .logo img {
            height: 40px !important;
        }

        .list {
/*            display: -webkit-flex;
            display: flex;*/
            height: 50px;
        }

        .nav {
            width: 100%;
        }

        .nav ul li a {
            padding: 0!important;
        }

        .nav ul li {
            width: 10%;
            text-align: center;
            line-height: 50px;
        }
    }

    @media screen and (max-width: 600px){
        html {
            overflow: hidden;
        }

        .nav {
            position: absolute;
            overflow: hidden;
            height: 50px;
        }

        .nav ul li {
            width: 20%;
        }
    }

</style>