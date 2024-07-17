/*
 * @Author       : Jay jay.zhangjunjie@outlook.com
 * @Date         : 2024-07-16 14:28:48
 * @LastEditTime : 2024-07-17 22:43:48
 * @LastEditors  : Jay jay.zhangjunjie@outlook.com
 * @Description  : MocaAPI C++ Appliction Imtegration | 未完待续
 */

#include <cstdint>
#include <iostream>
#include "MocapApi.h"





int main(int argc, const char** argv) {


    // MocaAPI
    std::cout << "-------" << std::endl;

    MocapApi::IMCPApplication *mcpApplication = nullptr;
    MocapApi::IMCPRenderSettings *mcpRenderSettings = nullptr;
    MocapApi::IMCPSettings *mcpSettings = nullptr;
    MocapApi::IMCPAvatar *mcpAvatar = nullptr;

    MocapApi::MCPGetGenericInterface(MocapApi::IMCPApplication_Version, reinterpret_cast<void**>(&mcpApplication));
    MocapApi::MCPGetGenericInterface(MocapApi::IMCPRenderSettings_Version, reinterpret_cast<void**>(&mcpRenderSettings));
    MocapApi::MCPGetGenericInterface(MocapApi::IMCPSettings_Version, reinterpret_cast<void**>(&mcpSettings));
    MocapApi::MCPGetGenericInterface(MocapApi::IMCPAvatar_Version, reinterpret_cast<void**>(&mcpAvatar));

    // 创建实体
    MocapApi::MCPRenderSettingsHandle_t mcpRenderSettingsHandel = 0;
    mcpRenderSettings->CreateRenderSettings(&mcpRenderSettingsHandel);


    // 创建设置
    MocapApi::MCPSettingsHandle_t mcpSettingsHandle = 0;
    mcpSettings->CreateSettings(&mcpSettingsHandle);
    mcpSettings->SetSettingsTCP("127.0.0.1", 7001, mcpSettingsHandle);



    MocapApi::MCPApplicationHandle_t mcpApplicationHandle = 0;
    mcpApplication->CreateApplication(&mcpApplicationHandle);
    mcpApplication->SetApplicationRenderSettings(mcpRenderSettingsHandel, mcpApplicationHandle);
    mcpApplication->SetApplicationSettings(mcpSettingsHandle, mcpApplicationHandle);




    mcpApplication->OpenApplication(mcpApplicationHandle);

    uint32_t numberOfAvatars = 0;
    MocapApi::EMCPError error = mcpApplication->GetApplicationAvatars(nullptr, &numberOfAvatars, mcpApplicationHandle);
    // error = mcpApplication->GetApplicationAvatars(nullptr, &numberOfAvatars, mcpApplicationHandle);
    if(error == MocapApi::Error_None){
        MocapApi::MCPAvatarHandle_t avatars = 0;
        error = mcpApplication->GetApplicationAvatars(&avatars, &numberOfAvatars, mcpApplicationHandle);
    }

    uint32_t jointsNum = 0;

    


    mcpApplication->CloseApplication(mcpApplicationHandle);
    mcpApplication->DestroyApplication(mcpApplicationHandle);

    return 0;
}