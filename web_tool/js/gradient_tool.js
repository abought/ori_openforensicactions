/**
 * Created by abought on 1/21/15.
 */

//"use strict";

var GradientTool = function(){
    // Store image data apart from canvas
    this.storedImage = new Image();
    var that = this;
    this.storedImage.onload = function(){that.imgToCanvas(this)};

    this.setElements = function(canvas, saveButton, gradientsBox){
        // Configure the divs required once page has loaded
        this.canvas = canvas;

        this.saveButton = saveButton;
        this.gradientsBox = gradientsBox;
    };


    this.imgToCanvas = function(imgData){
        // When an image is loaded, update the canvas drawing
        console.log("Event firing");

        var ctx = this.canvas.getContext('2d');

        this.canvas.width = imgData.width;
        this.canvas.height = imgData.height;
        ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        ctx.drawImage(imgData, 0, 0);

        this.greyScaleImg(this.canvas);

        // Once image is loaded, enable the save link
        this.saveButton.removeAttribute("disabled");
        this.gradientsBox.style.display = "";
    };

    this.imageFromURL = function(url){
        this.storedImage.src = url;
    };

    this.imageFromFileBlob = function(blob){
        if (!blob.type.match("image.*")) {
            console.log('Specified file blob is not an image')
        } else {
            var that = this;
            var reader = new FileReader();
            // Load file data to the image object
            reader.onload = function(event){
                that.storedImage.src = event.target.result;
            };
            reader.readAsDataURL(blob);
        }
    };

    this.renderFile = function(event){
        var img_blob = event.target.files[0];
        this.imageFromFileBlob(img_blob);
    };


    this.addGradient = function(grad_name, color_stops){
        // Add a new rectangular canvas with fill representing specified gradient

        var grdCanvas = document.createElement("canvas");
        grdCanvas.width = 256;
        grdCanvas.height = 20;

        var ctx = grdCanvas.getContext('2d');
        var grd = ctx.createLinearGradient(0, 0, grdCanvas.width, 0);

        for (var i=0; i < color_stops.length; i++){
            grd.addColorStop(color_stops[i][0], color_stops[i][1]);
        }
        ctx.fillStyle = grd;
        ctx.fillRect(0, 0, grdCanvas.width, grdCanvas.height);

        var container = document.createElement('div');
        var label = document.createTextNode(grad_name);
        container.appendChild(label);
        container.appendChild(grdCanvas);
        container.className = "gradient";

        this.gradientsBox.appendChild(container);

        // Add event listener only after gradient filled in
        var that = this;
        grdCanvas.onclick = function(){ that.recolorImg(this); //recolorImg(grdCanvas)
        };
    };

    this.greyScaleImg = function(){
        // Given a canvas rendering of an image, convert to greyscale
        var ctx = this.canvas.getContext("2d");

        var imageData = ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
        var data = imageData.data;

        for(var i = 0; i < data.length; i += 4) {
            var brightness = 0.34 * data[i] + 0.5 * data[i + 1] + 0.16 * data[i + 2];
            //YUV -> PAL/NTSC
            //var brightness = 0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2];
            data[i] = brightness; // red
            data[i + 1] = brightness; // green
            data[i + 2] = brightness; // blue
        }
        ctx.putImageData(imageData,0,0);
    };

    this.saveCanvas = function(linkEl){
        // Provide a link so the user can save the modified/ recolored image data to a file
        linkEl.href = this.canvas.toDataURL('image/png');
    };

    this.recolorImg = function(grdCanvas){
        // Apply the given gradient data to an image
        this.imgToCanvas(this.storedImage); // Always recolor from original image to avoid loss of color when two gradients applied in sequence

        var imgCtx = this.canvas.getContext('2d');
        var imgData = imgCtx.getImageData(0, 0, this.canvas.width, this.canvas.height);

        var imgOrig = imgData.data;
        var imgRecolor = imgData.data;

        var grdCtx = grdCanvas.getContext('2d');
        var grdData = grdCtx.getImageData(0, 0, grdCanvas.width, grdCanvas.height);
        var grdArr = grdData.data;

        // TODO: for every pixel in array,
        // colorization method from: http://podeplace.blogspot.com/2012/12/pseudocolorisation-with-javascript.html
        for(var y = 0; y < this.canvas.height; y++) {
            for (var x = 0; x < this.canvas.width; x++) {
                var index = (x + y * this.canvas.width) * 4;

                 //we grab the color from one channel (the red one)
                 var luminosityValue = imgOrig[index + 0];

                 //we retrieve the corresponding (R,G,B) triplet from the colormap
                 //we rewrite the new color
                 imgRecolor[index + 0] = grdArr[luminosityValue * 4 + 0]; //R
                 imgRecolor[index + 1] = grdArr[luminosityValue * 4 + 1]; //G
                 imgRecolor[index + 2] = grdArr[luminosityValue * 4 + 2]; //B
                 //dataRes[index+3] = 255; //no need to change alpha value
         }}
        imgData.data = imgRecolor;
        imgCtx.putImageData(imgData, 0, 0);
    }
};