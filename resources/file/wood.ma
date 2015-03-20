//Maya ASCII 2015 scene
//Name: wood.ma
//Last modified: Sun, Feb 22, 2015 01:24:26 AM
//Codeset: UTF-8
requires maya "2015";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2015";
fileInfo "version" "2015";
fileInfo "cutIdentifier" "201405190330-916664";
fileInfo "osv" "Mac OS X 10.9.5";
fileInfo "license" "student";
createNode place3dTexture -n "place3dTexture1";
createNode place3dTexture -n "place3dTexture2";
createNode blinn -n "wood";
	setAttr ".tc" 0.030303031206130981;
	setAttr ".rfl" 0.70707070827484131;
	setAttr ".sro" 0.69696968793869019;
createNode wood -n "wood1";
	setAttr ".v" 0.35400000214576721;
	setAttr ".ls" 0.097999997437000275;
	setAttr ".rd" 0.61799997091293335;
	setAttr ".a" 98;
	setAttr ".gx" 0.45500001311302185;
	setAttr ".gs" 0.017000000923871994;
	setAttr ".ax" 1;
	setAttr ".ay" 1;
	setAttr ".ra" 0.26399999856948853;
createNode stucco -n "stucco1";
	setAttr ".c1" -type "float3" 0.62699997 0.477 0.25799999 ;
	setAttr ".c2" -type "float3" 0.86299998 0.63599998 0.52399999 ;
createNode bump3d -n "bump3d1";
	setAttr ".bd" 0.0099999997764825821;
	setAttr ".bv" 0.086956523358821869;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -s 3 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 3 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 3 ".u";
select -ne :defaultRenderingList1;
select -ne :defaultTextureList1;
	setAttr -s 2 ".tx";
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "wood1.oc" "wood.c";
connectAttr "bump3d1.o" "wood.n";
connectAttr "place3dTexture1.wim" "wood1.pm";
connectAttr "stucco1.oc" "wood1.vc";
connectAttr "place3dTexture2.wim" "stucco1.pm";
connectAttr "wood.msg" ":defaultShaderList1.s" -na;
connectAttr "place3dTexture1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "place3dTexture2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "bump3d1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "wood1.msg" ":defaultTextureList1.tx" -na;
connectAttr "stucco1.msg" ":defaultTextureList1.tx" -na;
// End of wood.ma
