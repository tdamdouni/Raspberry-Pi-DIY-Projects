use <PiZero_1.2.scad>

$fn=120;
radius=20;
size=40;
drill=30;
	
pi_hole_distance_x =58;
pi_hole_distance_y =23;
	
module base()
{
	minkowski()
	{
		cube(size=[93,52,40],center=true);
		cylinder(r=radius,center=true);
	}
}

module zero_standoff(){
	
	//Pi Zero Standoffs
	difference(){
		
		union(){
			translate([-pi_hole_distance_y/2,-pi_hole_distance_x/2,-20])cylinder(r=6,h=21);
			translate([-pi_hole_distance_y/2,pi_hole_distance_x/2,-20])cylinder(r=6,h=21);
			translate([pi_hole_distance_y/2,-pi_hole_distance_x/2,-20])cylinder(r=6,h=21);
			translate([pi_hole_distance_y/2,pi_hole_distance_x/2,-20])cylinder(r=6,h=21);
		}
		
		translate([-pi_hole_distance_y/2,-pi_hole_distance_x/2,-10])cylinder(r=1,h=21);
		translate([-pi_hole_distance_y/2,pi_hole_distance_x/2,-10])cylinder(r=1,h=21);
		translate([pi_hole_distance_y/2,-pi_hole_distance_x/2,-10])cylinder(r=1,h=21);
		translate([pi_hole_distance_y/2,pi_hole_distance_x/2,-10])cylinder(r=1,h=21);
	}
	
}


module cover_drills(){
    	translate([-59,-27,0])cylinder(r=1.5,h=20);
    	translate([-59,-27,0])cylinder(r=1.5,h=20);
        translate([-59,27,0])cylinder(r=1.5,h=20);
        translate([59,-20,0])cylinder(r=1.5,h=20);
        translate([59,20,0])cylinder(r=1.5,h=20);
        translate([20,-30,0])cylinder(r=1.5,h=20);
        translate([20,30,0])cylinder(r=1.5,h=20);
}

module speaker_box(){
	difference(){
		base();

		translate([0,0,35])scale([0.955,0.925,0.925])base();

		//Speaker Cutout
		translate([-20,0,-15])cylinder(r=77.5/2,h=40);

		//Pi Zero Cutout
		translate([24,-35,-15])cube(size=[32,72,40]);
		
		//Mirco USB Hole
		translate([40,18,-0])cube(size=[30,12.5,10]);
		
		//Speaker Cable Hole
		translate([0,-2,-15])cube(size=[30,5,5]);

        //Camera Cable Cutouts
        translate([53,-15,-14])cube(size=[10,30,42]);
        translate([30, 36,-14])cube(size=[18,6.3,42]);
        translate([30, -40,-14])cube(size=[23,6,42]);

		//Speaker Drills
		translate([-20,0,5]){
			translate([-drill,drill,0])cylinder(r=1.5,h=20);
			translate([-drill,-drill,0])cylinder(r=1.5,h=20);
			translate([drill,-drill,0])cylinder(r=1.5,h=20);
			translate([drill,drill,0])cylinder(r=1.5,h=20);
		}
		
		//Cover Drills
		translate([0,0,5]){
            cover_drills();
		}
		
	}
	
	translate([40,2,0]) zero_standoff();

}


module grillHoles(){
	
	for(y=[1:14]){
		for(x=[1:15]){
			translate([x*5,y*5,0]) scale([1,1,3])cube(2);
		}
	}
}

module grill(clean=true, logo=false){
	
	difference(){
		union(){
			difference(){
				translate([0,0,0])scale([0.948,0.92,0.1])base();
				translate([0,0,-1.8])scale([0.88,0.85,0.1])base();
				
					translate([45,0,-10])cylinder(r=2,r2=10,h=20);
				
					//Microphone Holes
					translate([45,-28,-10])cylinder(r=2,r2=2,h=20);
					translate([45,28,-10])cylinder(r=2,r2=2,h=20);
			}	
		}


        if(clean == false){
            translate([-60,-38,0]){
                grillHoles();
            } 
        }else {
            translate([-20,0,-15])cylinder(r=70/2,h=40);
        }
        
        translate([0,0,-10]) cover_drills();
		
		//Logo
        if(logo == true){
            translate([25, 35,1]) {
                rotate([0,0,-90])scale([0.8,0.8,3])text("nyumaya.com", font = "Liberation Sans:style=Bold Italic");
            }
        }
	}
	
}

//speaker_box();
//translate([40,2,2]) rotate([0,0,90]) PiZeroBody();
translate([0,0,18.5]) grill();



