import pytest
import os

if __name__ == "__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['./Scripts', '--alluredir', './Report/report_data'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./Report/report_data -o ./Report/report --clean')
    os.system('powershell.exe  rmdir -r ./Report/report_data/* -Force')
    