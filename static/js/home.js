$(document).ready(function () {
  const $cont = $('.cont');
  const $slider = $('.slider');
  const $nav = $('.navslide');
  const winW = $(window).width();
  const animSpd = 750; // Change also in CSS

  const distOfLetGo = winW * 0.2;
  let curSlide = 1;
  let animation = false;
  let autoScrollVar = true;
  let diff = 0; // Generating slides
  let arrCities = []
// MY ADDITIONS
    let ids = $('#artists_ids').text()
    ids = ids.replace(/[^0-9]/g, '');
    for (var id=0; id<ids.length; id++) {
        let name  = $('#artist_'+ids[id]).text()
        arrCities.push(name);
    }
  // END ADDITIONS
  let slide_len = arrCities.length;

  let generateSlide = function (city) {
    let frag1 = $(document.createDocumentFragment());
    let frag2 = $(document.createDocumentFragment());
    const numSlide = arrCities.indexOf(arrCities[city]) + 1;
    const firstLetter = arrCities[city][0].charAt(0);
    const $slide = $(`<div data-target="${numSlide}" class="slide slide--${numSlide}">
							<div class="slide__darkbg slide--${numSlide}__darkbg"></div>
							<div class="slide__text-wrapper slide--${numSlide}__text-wrapper"></div>
						</div>`);
    const letter = $(`<div class="slide__letter slide--${numSlide}__letter">
							${firstLetter}
						</div>`);

    // for (let i = 0, length = arrCities[city].length; i < length; i++) {
      const text = $(`<div class="slide__text slide__text"><a href="/profile/${arrCities[city]}">
								${arrCities[city]}</a>
							</div>`);
      frag1.append(text);

    const navSlide = $(`<li data-target="${numSlide}" class="nav__slide nav__slide--${numSlide}"></li>`);
    frag2.append(navSlide);
    $nav.append(frag2);
    $slide.find(`.slide--${numSlide}__text-wrapper`).append(letter).append(frag1);
    $slider.append($slide);

    if (arrCities[city].length <= 4) {
      $('.slide--' + numSlide).find('.slide__text').css("font-size", "12vw");
    }
  };

  for (let i = 0, length = slide_len; i < length; i++) {
    generateSlide(i);
  }

  $('.nav__slide--1').addClass('nav-active'); // Navigation

  function bullets(dir) {
    $('.nav__slide--' + curSlide).removeClass('nav-active');
    $('.nav__slide--' + dir).addClass('nav-active');
  }

  function timeout() {
    animation = false;
  }

  function pagination(direction) {
    animation = true;
    diff = 0;
    $slider.addClass('animation');
    $slider.css({
      'transform': 'translate3d(-' + (curSlide - direction) * 100 + '%, 0, 0)'
    });
    $slider.find('.slide__darkbg').css({
      'transform': 'translate3d(' + (curSlide - direction) * 50 + '%, 0, 0)'
    });
    $slider.find('.slide__letter').css({
      'transform': 'translate3d(0, 0, 0)'
    });
    $slider.find('.slide__text').css({
      'transform': 'translate3d(0, 0, 0)'
    });
  }

  function navigateRight() {
    if (!autoScrollVar) return;
    if (curSlide >= slide_len) return;
    pagination(0);
    setTimeout(timeout, animSpd);
    bullets(curSlide + 1);
    curSlide++;
  }

  function navigateLeft() {
    if (curSlide <= 1) return;
    pagination(2);
    setTimeout(timeout, animSpd);
    bullets(curSlide - 1);
    curSlide--;
  }

  function toDefault() {
    pagination(1);
    setTimeout(timeout, animSpd);
  } // Events


  $(document).on('mousedown touchstart', '.slide', function (e) {
    if (animation) return;
    let target = +$(this).attr('data-target');
    let startX = e.pageX || e.originalEvent.touches[0].pageX;
    $slider.removeClass('animation');
    $(document).on('mousemove touchmove', function (e) {
      let x = e.pageX || e.originalEvent.touches[0].pageX;
      diff = startX - x;
      if (target === 1 && diff < 0 || target === slide_len && diff > 0) return;
      $slider.css({
        'transform': 'translate3d(-' + ((curSlide - 1) * 100 + diff / 30) + '%, 0, 0)'
      });
      $slider.find('.slide__darkbg').css({
        'transform': 'translate3d(' + ((curSlide - 1) * 50 + diff / 60) + '%, 0, 0)'
      });
      $slider.find('.slide__letter').css({
        'transform': 'translate3d(' + diff / 60 + 'vw, 0, 0)'
      });
      $slider.find('.slide__text').css({
        'transform': 'translate3d(' + diff / 15 + 'px, 0, 0)'
      });
    });
  });
  $(document).on('mouseup touchend', function (e) {
    $(document).off('mousemove touchmove');
    if (animation) return;

    if (diff >= distOfLetGo) {
      navigateRight();
    } else if (diff <= -distOfLetGo) {
      navigateLeft();
    } else {
      toDefault();
    }
  });
  $(document).on('click', '.nav__slide:not(.nav-active)', function () {
    let target = +$(this).attr('data-target');
    bullets(target);
    curSlide = target;
    pagination(1);
  });
  $(document).on('click', '.side-nav', function () {
    let target = $(this).attr('data-target');
    if (target  === 'right' && curSlide === slide_len){
      // pagination(1);
      // setTimeout(timeout, animSpd);
      console.log('rih')
    }
    else if (target === 'right'){ 
      console.log('rihg')
      navigateRight();}

    if (target === 'left') {
      navigateLeft()
      console.log('lih')
    };
  });
  $(document).on('keydown', function (e) {
    if (e.which === 39) navigateRight();
    if (e.which === 37) navigateLeft();
  });
  $(document).on('mousewheel DOMMouseScroll', function (e) {
    if (animation) return;
    let delta = e.originalEvent.wheelDelta;
    if (delta > 0 || e.originalEvent.detail < 0) navigateLeft();
    if (delta < 0 || e.originalEvent.detail > 0) navigateRight();
  });


  // MY ADDITIONS
  for (var id=0; id<ids.length; id++) {
    let image = $('#artist_img_'+ids[id]).text();
    $('.slide--'+(id+1)+'__darkbg').css({
        'left' : (id+1)*(-50)+50 + '%',
        'background' : 'url("media/' + image + '") center center no-repeat',
        'background-size' : 'cover',
        'background-position' : '0px center, 0px center',
        'transform' : 'translate3d(0, 0, 0)',
        'will-change' : 'transform'
    });
    
    $('.slide--'+(id+1)+'__darkbg:after').css({
        'content' : '""',
        'position' : 'absolute',
        'top' : '0',
        'left' : '0',
        'width' : '100%',
        'height' : '100%',
        'background-color' : 'rgba(11, 15, 39, 0.83)'
    });
    
    $('.slide--'+(id+1)+'__letter').css({
        'background' : 'url("media/' + image + '") center center no-repeat',
        'background-position' : '0px center, 0px center',
        'background-size' : 'cover'
    });
    $('.slide--'+(id+1)).css({
        'left' : id*100+'%'
    });
    

  }

  // if(id < slide_len){
  //     setTimeout(function(){
  //       navigateRight();
  //     }, 3000);
  //   }
  //   else{
  //     setTimeout(function(){
  //       toDefault();
  //     }, 3000);
  //   }

    // pagination(1);
    // setTimeout(timeout, animSpd);

    // if (!autoScrollVar) return;
    // if (curSlide == numOfCities){
    //   toDefault()
    //   curSlide = 1;
    // };
    // pagination(0);
    // setTimeout(timeout, animSpd);
    // bullets(curSlide + 1);
    // curSlide++;



// END ADDITIONS




});