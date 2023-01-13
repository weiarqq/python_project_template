from infra_sdk.cat_service import CatService




"""
对外接口




"""

if __name__ == '__main__':
    from config import config
    CatService(config.application.name, config.application.env)