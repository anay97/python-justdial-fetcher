a=$('p.contact-info').each(function(index){
$(this).find('span.icon-ba').replaceWith('-');
$(this).find('span.icon-dc').replaceWith('+');
$(this).find('span.icon-fe').replaceWith('(');
$(this).find('span.icon-hg').replaceWith(')');
$(this).find('span.icon-acb').replaceWith('0');
$(this).find('span.icon-yz').replaceWith('1');
$(this).find('span.icon-wx').replaceWith('2');
$(this).find('span.icon-vu').replaceWith('3');
$(this).find('span.icon-ts').replaceWith('4');
$(this).find('span.icon-rq').replaceWith('5');
$(this).find('span.icon-po').replaceWith('6');
$(this).find('span.icon-nm').replaceWith('7');
$(this).find('span.icon-lk').replaceWith('8');
$(this).find('span.icon-ji').replaceWith('9');
})