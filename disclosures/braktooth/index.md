---
layout: default_disclosure
title: BrakTooth
img: braktooth_logo.svg
img_size: 230px
comments: true
tags: [disclosure]
---

<script>
	function setDocHeight(ctx) { 
	    setTimeout(()=>{
	    	 doc = ctx.contentDocument || document;
	    	var body = doc.body, html = doc.documentElement;
	    	var height = Math.max( body.scrollHeight, body.offsetHeight, 
	        html.clientHeight, html.scrollHeight, html.offsetHeight );
	    	ctx.style.height = height + 'px';
	    },100);
}
</script>


<!-- <iframe src="header.html" style="width: 100%; max-height: 50px; margin-top: 20px ;margin-bottom: -100px" scrolling="no" frameBorder="0"></iframe> -->


<iframe name="iframe" id="iframeid" src="disclosure.html" style="height:100vh;width: 100%;" onload="setDocHeight(this)" scrolling="no" frameBorder="0"></iframe>

