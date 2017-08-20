var md = false;
var color = tinycolor('#000000');

$(document).ready(function(){

$.ajaxSetup({ cache: false });

$(document)
  .on('mousedown',function(e){md=true;})
  .on('mouseup',function(e){md=false;});


$('.palette li').on('click',function(){
  $('.palette li').removeClass('selected');
  $(this).addClass('selected');

  $('.current').css('background-color', current_color().toRgbString() );
  $('.mc').trigger("colorpickersliders.updateColor", current_color().toHexString());

}).each(function(){
  $(this).data('default', $(this).css('background-color'));
});

function current_color(){
  return color;
}


function is_target_color(obj){

  return ( tinycolor($(obj).css('background-color')).toRgbString() == fill_target);

}

function do_fill(obj){
  obj = $(obj);

  if( is_target_color(obj) ){

    update_pixel(obj, current_color());

    var r = obj.next('td');
    var l = obj.prev('td');
    var u = obj.parent().prev('tr').find('td:eq(' + obj.index() + ')');
    var d = obj.parent().next('tr').find('td:eq(' + obj.index() + ')');

    if( r.length && is_target_color(r[0]) ) fill_stack.push(r[0]);
    if( l.length && is_target_color(l[0]) ) fill_stack.push(l[0]);
    if( u.length && is_target_color(u[0]) ) fill_stack.push(u[0]);
    if( d.length && is_target_color(d[0]) ) fill_stack.push(d[0]);
  }
}

function save(){
  var filename = prompt('Please enter a filename', 'mypaint');
  filename = filename.replace(/[^a-z0-9]/gi, '_').toLowerCase();
  $.get('/save/' + filename);
  alert('Saved into saves/' + filename + '.py, \nRun with "sudo saves/' + filename + '.py"');
}

function clear(){
  $('td').css('background-color','rgb(0,0,0)').data('changed',false);
  $.get('/clear');
  $.get('/show');
}

function lighten(obj){
  var rgb = tinycolor($(obj).css('background-color')).toRgb();

  update_pixel(obj, tinycolor({
    r: rgb.r + 2,
    g: rgb.g + 2,
    b: rgb.b + 2
  }));
}

function darken(obj){
  var rgb = tinycolor($(obj).css('background-color')).toRgb();

  update_pixel(obj, tinycolor({
    r: rgb.r - 2,
    g: rgb.g - 2,
    b: rgb.b - 2
  }));
}

/*
function set_color(hex){
  $('.palette li.selected').css('background-color', rgb_string(rgb));
  $('.current').css('background-color',rgb_string(rgb));
}
*/

function pick(obj){
  var col = tinycolor($(obj).css('background-color'));
  $('.mc').trigger("colorpickersliders.updateColor", col.toHexString());
}

function update_pixel(obj, col){

  var bgcol = tinycolor($(obj).css('background-color'));

  if( col.toRgbString() != bgcol.toRgbString() ){
    $(obj)
      .data('changed', true)
      .css('background-color',col.toRgbString());
  }
}

function update_pixels(){
  var changed = false;
  $('td').each(function( index, obj ){
    if( $(obj).data('changed') ){
      $(obj).data('changed',false);
      changed = true;

      var x = $(this).index();
      var y = $(this).parent().index();
      var col = tinycolor($(obj).css('background-color')).toRgb();

      var data = [x,y,col.r,col.g,col.b];

      $.get('/pixel/' + data.join('/'));
    }
  });
  if(changed){
    $.get('/show');
  }
}

function update_pixels(){
  var changed = false;
  $('td').each(function( index, obj ){
    if( $(obj).data('changed') ){
      $(obj).data('changed',false);
      changed = true;

      var x = $(this).index();
      var y = $(this).parent().index();
      var col = tinycolor($(obj).css('background-color')).toRgb();

      var data = [col.r,col.g,col.b];

      $.get('/map/' + data.join('/'));
    }
  });
  if(changed){
    $.get('/show');
  }
}

function update_map(){
  var col = current_color().toRgb();
  var data = [col.r,col.g,col.b];

  $.get('/map/' + data.join('/'));
  $.get('/show');
  }


function paint(obj){
  update_pixel(obj, current_color());
}

$('table td').on('click',function(){
  handle_tool(this, true);
});
$('table td').on('mousemove',function(){
  if(!md) return false;
  handle_tool(this, false);
});

$('h1').on('mouseover',function(){
  update_pixel(this, current_color());
  console.log('Selected color',current_color().toRgb());
});



swatches = [
'rgb(0,0,0)','rgb(132,0,0)','rgb(0,132,0)','rgb(132,132,0)','rgb(0,0,132)','rgb(132,0,132)','rgb(0,132,132)','rgb(132,132,132)',
'rgb(198,198,198)','rgb(255,0,0)','rgb(0,255,0)','rgb(255,255,0)','rgb(0,0,255)','rgb(255,0,255)','rgb(0,255,255)','rgb(255,255,255)'
];

$('.mc').ColorPickerSliders({
  flat: true,
  previewformat: 'hex',
  color: current_color(),
  labels: {
    preview: '',
    hslhue: 'Hue',
    hslsaturation: 'Saturation',
    hsllightness: 'Lightness'
  },
  swatches: swatches,
  order: {
    hsl: 1,
    preview: 2
  },
  onchange: function(obj, c){
    color = c.tiny;
  }
});

$.get('/clear');
$.get('/show');

var update = setInterval(update_map, 50);
});


