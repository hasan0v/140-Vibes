
// HIGHLIGHT BORDER
const ripple = el => {
	let d = el.dataset.ripple.split('-'),
		 s = 'rgba(198, 131, 3, 0.4)',
		 e = 'rgba(198, 131, 3, 1)';
	d[2] = Number(d[2]) + 4;
	el.dataset.ripple = d.join('-');
	el.style.background = `radial-gradient(circle at ${d[0]}px ${d[1]}px, ${s} 0%, ${s} ${d[2]}%, ${e} ${d[2] + 0.1}%)`;
	
	window.requestAnimationFrame(() => {
		if (el.dataset.ripple && d[2] < 100) ripple(el)
	});
};

const start = ev => {
	ev.target.dataset.ripple = `${ev.offsetX}-${ev.offsetY}-0`
	ripple(ev.target);
};

const stop = ev => {
	let ev = document.querySelector('[data-ripple]');
	delete ev.dataset.ripple;
	ev.style.background = 'none';
};

// Events
document.querySelectorAll('.highlight').forEach( el => el.addEventListener( 'mousedown', start ));
document.addEventListener( 'mouseup', stop );

var Winsize = function(){
    var win = $(window);
    if (win.width() <= 767 ) {
        $('#logo').css({
            'width' : '50',
            'height' : '50',
            'position' : 'relative',
            'top' : '5px',
            'left' : '2rem',
            'z-index' : '21'
        });
    }
    else {
        $('#logo').css({
            'width' : '60',
            'height' : '60',
            'position' : 'relative',
            'top' : '0rem',
            'left' : '4rem',
            'z-index' : '21'
        });
    }
}
$(window).resize(Winsize);  
$(document).ready(Winsize);

$(document).ready(function(){
    if (history.length>1) {
        $(".go_back").show()
    } else {
        $(".go_back").hide()
    }
})
