---
layout: default
title: CVEs
---

<!---
Insert here more iframes when needed.
The iframe should automatically ajust its size after 100ms
-->

<iframe src="disclosures/disclosures.html" style="width: 100%;height: 0px" onload="setDocHeight(this);" scrolling="no" frameBorder="0"></iframe>



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