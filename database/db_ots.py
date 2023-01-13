from tablestore import *
import cat


class DBOTS(object):
    def __init__(self, config):
        end_point = config.end_point
        access_key_id = config.access_key_id
        access_key_secret = config.access_key_secret
        instance_name = config.instance_name
        self.ots_client = OTSClient(end_point=end_point, access_key_id=access_key_id,
                                    access_key_secret=access_key_secret, instance_name=instance_name)

        self.table_name = config.table_name
        self.index_name = config.index_name  # 含website 主键

    @cat.transaction('SQL', 'ots_query')
    def query(self, docid, columns_to_get):
        primary_key = [('docid', docid)]
        consumed, return_row, _ = self.ots_client.get_row(self.table_name, primary_key, columns_to_get)
        if return_row:
            item = dict([(e[0], e[1]) for e in return_row.attribute_columns])
            return item
        return {}
