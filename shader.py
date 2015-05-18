from bge import logic
import time
import math

VertexShader = """
uniform float timer;

float rand(vec2 co){
    return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}
void main()
{
    gl_TexCoord[0] = gl_MultiTexCoord0;
    vec4 v=gl_Vertex;

	vec2 n=vec2(v.x+timer,v.x);
	float f;
	f=rand(n);
	n=fmod(n,2);
	v.z+=sin((v.x+v.y+timer)/2.);
	
	n=vec2(v.y+timer,v.y);
	f=rand(n);
	n=fmod(n,2);
	//v.y+=sin(v.y+timer);
    //v.y+=sin(timer)*1.0*n;
	//v.x+=n;
    
    gl_Position=gl_ModelViewProjectionMatrix *v;
}
"""

FragmentShader = """
uniform float timerfrag;
float rand(vec2 co){
    return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}
void main(void)
{
    //vec4 color=texture2D(colorMap,gl_TexCoord[0].st);
    float t;
    vec4 frag=gl_FragCoord;
    t=1; //timerfrag;
    gl_FragColor=vec4(t,0,0,0);
}
"""

def test():
	ShaderObject = logic.getCurrentController().owner

	mesh=ShaderObject.meshes[0]
	for material in mesh.materials:
		shader=material.getShader()
		if shader!=None:
			#if not shader.isValid():
			#print(shader)
			shader.setSource(VertexShader,FragmentShader,1)
				#shader.setSampler('colorMap',0)
			  
			t=time.time();
			tfrag=math.fmod(t,1)
			tvert=math.fmod(t,10000)
			print(tvert)
			shader.setUniform1f('timer',tvert)
			shader.setUniform1f('timerfrag',tfrag)        