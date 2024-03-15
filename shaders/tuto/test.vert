#version 330 core

layout (location = 0) in vec2 in_texcoord;
layout (location = 1) in vec3 in_normal;
layout (location = 2) in vec3 in_position;

out vec2 uv;
out vec3 normal;
out vec3 fragPos;
out vec4 shadowCoord;

uniform mat4 m_projection;
uniform mat4 m_view;
uniform mat4 m_view_light;
uniform mat4 m_model;

mat4 m_shadow_bias = mat4(
    0.5, 0.0, 0.0, 0.0,
    0.0, 0.5, 0.0, 0.0,
    0.0, 0.0, 0.5, 0.0,
    0.5, 0.5, 0.5, 1.0
);

void main() {
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
    normal = mat3(transpose(inverse(m_model))) * normalize(in_normal);
    uv = in_texcoord;
    fragPos = vec3(m_model * vec4(in_position, 1.0));
    
    mat4 shadowMVP = m_projection * m_view_light * m_model;
    shadowCoord = m_shadow_bias * shadowMVP * vec4(in_position, 1.0);
    shadowCoord.z -= 0.0005;
}
