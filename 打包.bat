@echo off
setlocal

rem 将工作目录放到系统临时目录，避免仓库残留
set "WORKPATH=%TEMP%\GenGoodsJpg_build"

pyinstaller --onefile --name GenGoodsJpg --paths src src\GenClothingJpgManager.py --distpath . --workpath "%WORKPATH%" --noconfirm --clean

rem 仅在构建成功后清理工作目录
if %ERRORLEVEL% EQU 0 (
    if exist "%WORKPATH%" rmdir /s /q "%WORKPATH%"
) else (
    echo 构建失败，保留工作目录以便排查：%WORKPATH%
)

endlocal
