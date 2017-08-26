//  Pi Zero model for checking other models
//  0,0,0 is centre of PCB, bottom face
//  This model is for V1.2

// PCB size variables
PiSizeX = 65;
PiSizeY = 30;
PiSizeZ = 1.5;
PiCornerRad = 3.0;
PiHoleEdge = 3.5;       // Mount holes are 3.5mm from each edge
PiHoleDia = 2.75;
PiHoleRad = PiHoleDia / 2;
PiHoleClearRad = 3.0;    // Mount holes have 6 Dia clear on PCB

//  Component connector centrelines from Pi centreline
PiSDX = -24.5;          // SD holder
PiSDY = 1.9;
PiUSBX = 8.9;           // Data (USB)
PiUSBY = -13;
PiOTGX = 21.5;          // Power (OTG)
PiOTGY = -13;
PiHDMIX = -20.1;        // HDMI
PiHDMIY = -11.4;

//  Component connector sizes
PiSDsizeX = 11.5;
PiSDsizeY = 12.0;
PiSDsizeZ = 1.3;
PiUSBsizeX = 7.5;
PiUSBsizeY = 5.0;
PiUSBsizeZ = 2.5;
PiHDMIsizeX = 11.25;
PiHDMIsizeY = 7.25;
PiHDMIsizeZ = 3.3;

//  SOC centrelines and sizes
PiSOCX = -2.5;
PiSOCY = -2;
PiSOCsizeX = 12;
PiSOCsizeY = 12;
PiSOCsizeZ = 1.2;

//  PP pads (on underside) centres from Pi centreline
// all Pi <padname> X, Y, D & C
// PP1 +5V
PiPP1X = 21.0;
PiPP1Y = -8.7;
PiPP1D = 2.25;
PiPP1C = "Red";
// PP6 GND
PiPP6X = 21.25;
PiPP6Y = -11.1;
PiPP6D = 2.25;
PiPP6C = "Black";
// PP22 Data +
PiPP22X = 9.4;
PiPP22Y = -13;
PiPP22D = 1.75;
PiPP22C = "Violet";
// PP23 Data -
PiPP23X = 7.4;
PiPP23Y = -13;
PiPP23D = 1.75;
PiPP23C = "Salmon";

//  Mount hole dims from centre lines
PiHoleX = PiSizeX/2 - PiHoleEdge;
PiHoleY = PiSizeY/2 - PiHoleEdge;

//
// Modules used for Pi model
//
module PiDrawPad(Xpos,Ypos,Di,Col)    // Places a spot at test pad point, coloured to show pad function
{
translate([Xpos,Ypos,PiSizeZ/4])
    color(Col)
    cylinder(h=PiSizeZ*2/3,d=Di,center=true);
}

module PiPCBhole(Xpos,Ypos)   // Cuts a hole through PCB
{
translate([Xpos,Ypos,PiSizeZ/2])
    cylinder(h=2*PiSizeZ,d=PiHoleDia,center=true);
}

module PiComponent(Xpos,Ypos,Xsize,Ysize,Zsize,Col)    // Makes a block to represent a component on the upper face
{
translate([Xpos,Ypos,PiSizeZ + Zsize/2]) color(Col)
    cube([Xsize,Ysize,Zsize], center=true);
}

//
//  This is the main routine and can be called from outside
//
module PiZeroBody() // Models the Pi.
{
color("Green")
difference()
    {
    hull()  // PCB shape
        {
        translate([-PiHoleX,-PiHoleY,PiSizeZ/2])
            cylinder(r=PiCornerRad,h=PiSizeZ,center=true);
        translate([PiHoleX,-PiHoleY,PiSizeZ/2])
            cylinder(r=PiCornerRad,h=PiSizeZ,center=true);
        translate([PiHoleX,PiHoleY,PiSizeZ/2])
            cylinder(r=PiCornerRad,h=PiSizeZ,center=true);
        translate([-PiHoleX,PiHoleY,PiSizeZ/2])
            cylinder(r=PiCornerRad,h=PiSizeZ,center=true);
        }
 
    // Corner screw holes
    PiPCBhole(-PiHoleX,-PiHoleY);
    PiPCBhole(PiHoleX,-PiHoleY);
    PiPCBhole(PiHoleX,PiHoleY);
    PiPCBhole(-PiHoleX,PiHoleY);
    // GPIO holes
    for (Xcount = [-10:10], Ycount = [-1:2:1])
        translate([Xcount*2.54,PiHoleY+Ycount*1.27,PiSizeZ/2])
            cylinder(h=2*PiSizeZ,d=1.2,center=true);
    // The other 4 holes (loop values cheat for simplicity)
    for (Xcount = [9:10], Ycount = [-5:2:-3])
        translate([Xcount*2.54,PiHoleY+Ycount*1.27,PiSizeZ/2])
            cylinder(h=2*PiSizeZ,d=1.2,center=true);
    }
    
PiComponent(PiSOCX,PiSOCY,PiSOCsizeX,PiSOCsizeY,PiSOCsizeZ,"Black");   // Processor
PiComponent(PiSDX,PiSDY,PiSDsizeX,PiSOCsizeY,PiSOCsizeZ,"Silver");   // SD card
PiComponent(PiHDMIX,PiHDMIY,PiHDMIsizeX,PiHDMIsizeY,PiHDMIsizeZ,"Silver");   // HDMI
PiComponent(PiUSBX,PiUSBY,PiUSBsizeX,PiUSBsizeY,PiUSBsizeZ,"Silver");   // USB
PiComponent(PiOTGX,PiOTGY,PiUSBsizeX,PiUSBsizeY,PiUSBsizeZ,"Silver");   // Power
}

//
//  This routine can be called separately from outside
//
module PiZeroTestPads()   //Show test pads for debugging connectors
{
    PiDrawPad(PiPP1X,PiPP1Y,PiPP1D,PiPP1C);
    PiDrawPad(PiPP6X,PiPP6Y,PiPP6D,PiPP6C);
    PiDrawPad(PiPP22X,PiPP22Y,PiPP22D,PiPP22C);
    PiDrawPad(PiPP23X,PiPP23Y,PiPP23D,PiPP23C);
}

/*
End of Pi model routines
Program from here
*/

// Input variables
ShowPiZero = true;
//ShowPiZero = false;
ShowTestPads = true;
// ShowTestPads = false;

// Overall definition
$fn=60;


// Model the Zero if required
if(ShowPiZero) PiZeroBody();

// Model the test pads if required
if (ShowTestPads) PiZeroTestPads();
