import argparse


def get_args(data_dir, cache_dir, embedding_folder, model_dir, log_dir):

    parser = argparse.ArgumentParser(description='RACE')

    parser.add_argument("--model_name", default="GAReader",
                        type=str, help="这批参数所属的模型的名字")

    parser.add_argument("--seed", default=3456, type=int, help="随机种子")

    # data_util
    parser.add_argument(
        "--data_path", default=data_dir, type=str, help="RACE数据集位置")

    parser.add_argument(
        "--cache_path", default=cache_dir, type=str, help="数据缓存地址"
    )

    parser.add_argument(
        "--sequence_length", default=60, type=int, help="句子长度"
    )

    # 输出文件名
    parser.add_argument(
        "--model_dir", default=model_dir + "GAReader/", type=str, help="输出模型的保存地址"
    )
    parser.add_argument(
        "--log_dir", default=log_dir + "GAReader/", type=str, help="日志文件地址"
    )

    parser.add_argument("--do_train",
                        action='store_true',
                        help="Whether to run training.")

    parser.add_argument("--print_step", default=1000,
                        type=int, help="多少步存储一次模型")
                        
    # 优化参数
    parser.add_argument("--batch_size", default=32, type=int)
    parser.add_argument("--epoch_num", default=4, type=int)
    parser.add_argument("--dropout", default=0.4, type=float)

    # 模型参数
    parser.add_argument("--output_dim", default=4, type=int)


    # word Embedding
    parser.add_argument(
        '--glove_word_file',
        default=embedding_folder + 'glove.840B.300d.txt',
        type=str, help='path of word embedding file')
    parser.add_argument(
        '--glove_word_size',
        default=int(2.2e6), type=int,
        help='Corpus size for Glove')
    parser.add_argument(
        '--glove_word_dim',
        default=300, type=int,
        help='word embedding size (default: 300)')

    config = parser.parse_args()

    return config
