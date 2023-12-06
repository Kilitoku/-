_base_ = ['co_dino_5scale_r50_lsj_8xb2_3x_coco.py']

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    type='CoDETR',
    _delete_=True,
    roi_head = dict(
        bbox_head=dict(
            num_classes=8
                      ),
        mask_head=dict(
            num_classes=8
                      )
                  )
            )

# Modify dataset related settings
dataset_type = 'CocoDataset'
data_root = 'data/coco/'
backend_args = None
data = dict(
    train=dict(
        data_root=data_root,
        img_prefix='train2017/',  
        ann_file='annotations/instances_train2017.json'),
    val=dict(
        data_root=data_root,
        img_prefix='val2017/',
        ann_file='annotations/instances_val2017.json'),
    test=dict(
        data_root=data_root,
        img_prefix='test2017/',
        ann_file=data_root + 'annotations/image_info_test-dev2017.json'))

test_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='Resize', scale=(1333, 800), keep_ratio=True)]

test_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file=data_root + 'annotations/image_info_test-dev2017.json',
        data_prefix=dict(img='test2017/'),
        test_mode=True,
        pipeline=test_pipeline))
        
test_evaluator = dict(
    type='CocoMetric',
    metric='bbox',
    format_only=True,
    ann_file=data_root + 'annotations/image_info_test-dev2017.json',
    outfile_prefix='./work_dirs/coco_detection/test')


