#version 330 core

layout (location = 2) in vec3 in_position;

uniform mat4 projection;
uniform mat4 view_light;
uniform mat4 model;

void main() {
    mat4 mvp = projection * view_light * model;
    gl_Position = mvp * vec4(in_position, 1.0);
}