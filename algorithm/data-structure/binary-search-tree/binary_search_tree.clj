(ns binary-search-tree
  (:require [clojure.pprint :as pp]))

(defrecord Node [value left right])

(defn bst-insert
  [tree val]
  (cond
    (nil? tree) (->Node val nil nil)
    (< val (:value tree)) (assoc tree :left (bst-insert (:left tree) val))
    (> val (:value tree)) (assoc tree :right (bst-insert (:right tree) val))
    :else tree))

(defn bst-find
  [tree val]
  (cond
    (nil? tree) nil
    (= val (:value tree)) tree
    (< val (:value tree)) (bst-find (:left tree) val)
    :else (bst-find (:right tree) val)))

(defn min-value-node
  [tree]
  (if (:left tree)
    (min-value-node (:left tree))
    tree))

(defn bst-delete
  [tree val]
  (cond
    (nil? tree) nil
    (< val (:value tree)) (assoc tree :left (bst-delete (:left tree) val))
    (> val (:value tree)) (assoc tree :right (bst-delete (:right tree) val))
    :else ;; 値が見つかった場合
    (cond
      (nil? (:left tree)) (:right tree) ;; 右の子がいる場合
      (nil? (:right tree)) (:left tree) ;; 左の子がいる場合
      :else
      (let [min-node (min-value-node (:right tree))]
        (assoc tree
               :value (:value min-node)
               :right (bst-delete (:right tree) (:value min-node)))))))

(defn -main []
  (let [tree (-> nil
                 (bst-insert 2)
                 (bst-insert 4)
                 (bst-insert 5)
                 (bst-insert 20)
                 (bst-insert 11)
                 (bst-insert 13)
                 (bst-insert 15))]
    (println "BST:")
    (pp/pprint tree)

    (println "\n検索 (4):" (bst-find tree 4))
    (println "検索 (10):" (bst-find tree 10))


    (let [tree (bst-delete tree 13)]
      (println "\n削除 (13) 後のBST:")
      (pp/pprint tree))))

(-main)
