import logging
 
# ロガーを取得する
logger = logging.getLogger("log_machine")
logger.setLevel(logging.DEBUG) # 出力レベルを設定
 
# ハンドラー1を生成する
h1 = logging.StreamHandler()
h1.setLevel(logging.DEBUG) # 出力レベルを設定
 
# ハンドラー2を生成する
h2 = logging.FileHandler('logging.log')
h2.setLevel(logging.ERROR) # 出力レベルを設定
 
# フォーマッタを生成する
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
# ハンドラーにフォーマッターを設定する
h1.setFormatter(fmt)
h2.setFormatter(fmt)
 
# ロガーにハンドラーを設定する
logger.addHandler(h1)
logger.addHandler(h2)
 
# ログ出力を行う
logger.debug("degubログを出力")
logger.info("infoログを出力")
logger.warn("warnログを出力")
logger.error("errorログを出力")