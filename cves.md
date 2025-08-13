---
layout: default
title: Disclosures
---

<script>
 function setDocHeight(ctx) {
  doc = ctx.contentDocument || document;
     var body = doc.body, html = doc.documentElement;
     var height = Math.max( body.scrollHeight, body.offsetHeight,
     html.clientHeight, html.scrollHeight, html.offsetHeight );
     ctx.style.height = height + 'px';
     
     setTimeout(()=>{
       doc = ctx.contentDocument || document;
      var body = doc.body, html = doc.documentElement;
      var height = Math.max( body.scrollHeight, body.offsetHeight,
         html.clientHeight, html.scrollHeight, html.offsetHeight );
      ctx.style.height = height + 'px';
     },100);
}
</script>

<!---
Insert here more iframes when needed.
The iframe should automatically ajust its size after 100ms
-->

<iframe src="disclosures/disclosures.html" style="height:100vh;width: 100%;" onload="setDocHeight(this);" scrolling="no" frameBorder="0"></iframe>
