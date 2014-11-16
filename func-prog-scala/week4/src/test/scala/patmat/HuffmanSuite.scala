package patmat

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

import patmat.Huffman._

@RunWith(classOf[JUnitRunner])
class HuffmanSuite extends FunSuite {
  trait TestTrees {
    val t1 = Fork(Leaf('a', 2), Leaf('b', 3), List('a', 'b'), 5)
    val t2 = Fork(Fork(Leaf('a', 2), Leaf('b', 3), List('a', 'b'), 5), Leaf('d', 4), List('a', 'b', 'd'), 9)
  }

  test("weight of a larger tree") {
    new TestTrees {
      assert(weight(t1) === 5)
    }
  }

  test("chars of a larger tree") {
    new TestTrees {
      assert(chars(t2) === List('a', 'b', 'd'))
    }
  }

  test("string2chars(\"hello, world\")") {
    assert(string2Chars("hello, world") === List('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd'))
  }

  test("occurrence counting with times()") {
    assert(times(List[Char]()) === List())
    assert(times(List('a', 'a', 'b', 'b', 'c')) === List(('a', 2), ('b', 2), ('c', 1)))
    assert(times(List('z', 'q', 'q', 'q')) === List(('z', 1), ('q', 3)))
  }

  test("makeOrderedLeafList for some frequency table") {
    assert(makeOrderedLeafList(List(('t', 2), ('e', 1), ('x', 3))) === List(Leaf('e', 1), Leaf('t', 2), Leaf('x', 3)))
  }
  
  test("singleton recognition") {
    assert(singleton(List()) === false)
    assert(singleton(List(Leaf('a', 1))) === true)
    assert(singleton(List(Leaf('a', 1), Leaf('b', 1))) === false)
    assert(singleton(List(Fork(Leaf('a', 1), Leaf('b', 1), List('a', 'b'), 2))) === true)
  }

  test("combine of some leaf list") {
    val leaflist = List(Leaf('e', 1), Leaf('t', 2), Leaf('x', 4))
    assert(combine(leaflist) === List(Fork(Leaf('e', 1), Leaf('t', 2), List('e', 't'), 3), Leaf('x', 4)))
  }
  
  test("check if createCodeTree works") {
    assert(createCodeTree(string2Chars("c")) === Leaf('c', 1))
    assert(createCodeTree(string2Chars("momo")) === Fork(Leaf('m', 2), Leaf('o', 2), List('m', 'o'), 4))
    assert(createCodeTree(string2Chars("motto")) === Fork(Fork(Leaf('m', 1), Leaf('o', 2), List('m', 'o'), 3), Leaf('t', 2), List('m', 'o', 't'), 5))
  }
  
  test("check if decode works properly...") {
    new TestTrees {
      assert(decode(t1, List(0, 1, 0, 1)) === List('a', 'b', 'a', 'b'))
      assert(decode(t2, List(1, 0, 1, 0, 0)) === List('d', 'b', 'a'))
    }
  }

  test("decode and encode a very short text should be identity") {
    new TestTrees {
      assert(decode(t1, encode(t1)("ab".toList)) === "ab".toList)
    }
  }
}
