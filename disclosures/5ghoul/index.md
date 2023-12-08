---
layout: default_disclosure
title: 5Ghoul
img: 5ghoul-logo.png
img_size: 195px
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


<iframe name="iframe" id="iframeid" src="disclosure.html" style="height:100vh;width: 100%;" onload="setDocHeight(this)" scrolling="no" frameBorder="0"></iframe>

