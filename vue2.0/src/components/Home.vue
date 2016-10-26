<template>
	<div class="wrap-article">
	    <ul v-for="item in article_list" id="content">
	    	<li class="article">
	    		<h1>{{ item.title }}</h1>
	    		<img v-bind:src="item.imgs">
	    		<p v-html="item.article"></p>
	    	</li>
	    </ul>
	</div>    
</template>
<script>
	export default {
		data: function(){
			return {
				apiUrl: "http://127.0.0.1:8000/api/article_list",
				article_list: null,
			}
		},
		mounted: function(){
			this.getData()
		},
		methods: {
			getData: function(){
				this.$http.get(this.apiUrl).then(function(response){
					const data = response.body;
                    this.article_list = data;
				},function(response){
					console.log('error')
				});				
			}
		},
		computed: {

		}
	}
</script>