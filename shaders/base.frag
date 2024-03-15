#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv ;
in vec3 normal;
in vec3 fragPos;
in vec4 shadowCoord;

struct Light {
    vec3 position;
    vec3 I_ambiant;
    vec3 I_diffuse;
    vec3 I_specular;
};

uniform Light light;
uniform sampler2D u_texture ;
uniform vec3 camPos;
uniform sampler2DShadow shadowMap;
uniform vec2 u_resolution;


float lookup(float ox, float oy) {
    vec2 pixelOffset = 1 / u_resolution;
    return textureProj(shadowMap, shadowCoord + vec4(ox * pixelOffset.x * shadowCoord.w,
                                                     oy * pixelOffset.y * shadowCoord.w, 0.0, 0.0));
}


float getSoftShadow(int n) {
    float shadow;
    float swidth = 0.6;
    float endp = swidth * 3.0 + swidth / 2.0;
    for (float y = -endp; y <= endp; y += swidth) {
        for (float x = -endp; x <= endp; x += swidth) {
            shadow += lookup(x, y);
        }
    }
    return shadow / n;
}


float getShadow() {
    float shadow = textureProj(shadowMap, shadowCoord);
    return shadow;
}


vec3 getLight(vec3 color) {
    vec3 Normal = normalize(normal);

    vec3 ambiant = light.I_ambiant;

    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * light.I_diffuse;

    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 specular = spec * light.I_specular;

    float shadow = getSoftShadow(12);

    return color * (ambiant + (diffuse + specular) * shadow);
}


void main() {
    float gamma = 2.2;
    vec3 color = texture(u_texture , uv ).rgb;
    color = pow(color, vec3(gamma));

    color = getLight(color);

    color = pow(color, 1 / vec3(gamma));
    fragColor = vec4(color, 1.0);

}











