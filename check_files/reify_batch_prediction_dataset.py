    from bigml.api import BigML
    api = BigML()
    source1_file = "iris.csv"
    args = \
        {u'fields': {u'000000': {u'name': u'sepal length', u'optype': u'numeric'},
                     u'000001': {u'name': u'sepal width', u'optype': u'numeric'},
                     u'000002': {u'name': u'petal length', u'optype': u'numeric'},
                     u'000003': {u'name': u'petal width', u'optype': u'numeric'},
                     u'000004': {u'name': u'species',
                                 u'optype': u'categorical',
                                 u'term_analysis': {u'enabled': True}}}}
    source2 = api.create_source(source1_file, args)
    api.ok(source2)
    
    args = \
        {u'objective_field': {u'id': u'000004'}}
    dataset1 = api.create_dataset(source2, args)
    api.ok(dataset1)
    
    args = \
        {u'split_candidates': 32}
    model1 = api.create_model(dataset1, args)
    api.ok(model1)
    
    args = \
        {u'fields_map': {u'000001': u'000001',
                         u'000002': u'000002',
                         u'000003': u'000003',
                         u'000004': u'000004'},
         u'operating_kind': u'probability',
         u'output_dataset': True}
    batchprediction1 = api.create_batch_prediction(model1, dataset1, args)
    api.ok(batchprediction1)
    
    dataset2 = api.get_dataset(batchprediction1["object"]["output_dataset_resource"])
    api.ok(dataset2)
    
    args = \
        {u'fields': {u'100000': {u'name': u'species', u'preferred': True}},
         u'objective_field': {u'id': u'100000'}}
    dataset3 = api.update_dataset(dataset2, args)
    api.ok(dataset3)
    