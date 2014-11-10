package funsets

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

/**
 * This class is a test suite for the methods in object FunSets. To run
 * the test suite, you can either:
 *  - run the "test" command in the SBT console
 *  - right-click the file in eclipse and chose "Run As" - "JUnit Test"
 */
@RunWith(classOf[JUnitRunner])
class FunSetSuite extends FunSuite {

  /**
   * Link to the scaladoc - very clear and detailed tutorial of FunSuite
   *
   * http://doc.scalatest.org/1.9.1/index.html#org.scalatest.FunSuite
   *
   * Operators
   *  - test
   *  - ignore
   *  - pending
   */

  /**
   * Tests are written using the "test" operator and the "assert" method.
   */
  test("string take") {
    val message = "hello, world"
    assert(message.take(5) == "hello")
  }

  /**
   * For ScalaTest tests, there exists a special equality operator "===" that
   * can be used inside "assert". If the assertion fails, the two values will
   * be printed in the error message. Otherwise, when using "==", the test
   * error message will only say "assertion failed", without showing the values.
   *
   * Try it out! Change the values so that the assertion fails, and look at the
   * error message.
   */
  test("adding ints") {
    assert(1 + 2 === 3)
  }

  import FunSets._

  test("contains is implemented") {
    assert(contains(x => true, 100))
  }

  /**
   * When writing tests, one would often like to re-use certain values for multiple
   * tests. For instance, we would like to create an Int-set and have multiple test
   * about it.
   *
   * Instead of copy-pasting the code for creating the set into every test, we can
   * store it in the test class using a val:
   *
   *   val s1 = singletonSet(1)
   *
   * However, what happens if the method "singletonSet" has a bug and crashes? Then
   * the test methods are not even executed, because creating an instance of the
   * test class fails!
   *
   * Therefore, we put the shared values into a separate trait (traits are like
   * abstract classes), and create an instance inside each test method.
   *
   */

  trait TestSets {
    def pos(x: Int): Boolean = x > 0
    def neg(x: Int): Boolean = x < 0
    def even(x: Int): Boolean = x % 2 == 0
    def odd(x: Int): Boolean = x % 2 != 0
    def plus(x: Int) = x + 1
    def minus(x: Int) = x - 1
    def square(x: Int) = x * x
    val s1 = singletonSet(1)
    val s2 = singletonSet(2)
    val s3 = singletonSet(3)
  }

  /**
   * This test is currently disabled (by using "ignore") because the method
   * "singletonSet" is not yet implemented and the test would fail.
   *
   * Once you finish your implementation of "singletonSet", exchange the
   * function "ignore" by "test".
   */
  test("singletonSet(1) contains 1") {

    /**
     * We create a new instance of the "TestSets" trait, this gives us access
     * to the values "s1" to "s3".
     */
    new TestSets {
      /**
       * The string argument of "assert" is a message that is printed in case
       * the test fails. This helps identifying which assertion failed.
       */
      assert(contains(s1, 1), "Singleton")
    }
  }

  test("union contains all elements") {
    new TestSets {
      val s = union(s1, s2)
      assert(contains(s, 1), "Union 1")
      assert(contains(s, 2), "Union 2")
      assert(!contains(s, 3), "Union 3")
    }
  }

  test("Intersect works properly") {
    new TestSets {
      val f = union(s1, s2)
      val s = union(s2, s3)
      val f_inter_s = intersect(f, s)
      assert(contains(f_inter_s, 2), "Intersection contains 2")
      assert(!contains(f_inter_s, 1), "Intersection doesn't contain 3")
      assert(!contains(f_inter_s, 3), "Intersection doesn't contain 1")
    }
  }

  test("Difference works properly") {
    new TestSets {
      val f = union(s1, s2)
      val s = union(s2, s3)
      val f_minus_s = diff(f, s)
      assert(contains(f_minus_s, 1), "Difference contains 1")
      assert(!contains(f_minus_s, 2), "Difference doesn't contain 2")
      assert(!contains(f_minus_s, 3), "Difference doesn't contain 3")
    }
  }

  test("Filter works properly") {
    new TestSets {
      val f = union(s1, union(s2, s3))
      assert(contains(filter(f, pos), 1), "1 is > 0")
      assert(contains(filter(f, pos), 2), "2 is > 0")
      assert(contains(filter(f, pos), 3), "3 is > 0")
      assert(!contains(filter(f, neg), 1), "1 is < 0")
      assert(!contains(filter(f, neg), 2), "2 is < 0")
      assert(!contains(filter(f, neg), 3), "3 is < 0")
      assert(!contains(filter(f, even), 1), "1 is odd")
      assert(contains(filter(f, even), 2), "2 is even")
      assert(!contains(filter(f, even), 3), "3 is odd")
      assert(contains(filter(f, odd), 1), "1 is odd")
      assert(!contains(filter(f, odd), 2), "2 is even")
      assert(contains(filter(f, odd), 3), "3 is odd")
    }
  }

  test("Forall works properly") {
    new TestSets {
      val f = union(s1, union(s2, s3))
      val g = union(s1, s3)
      assert(forall(f, pos), "Positive number set")
      assert(!forall(f, neg), "Positive number set")
      assert(!forall(f, even), "Set{1,2,3} contains odd numbers")
      assert(forall(g, odd), "Set{1, 3} has only odd numbers")
    }
  }
  
  test("Exists works properly") {
    new TestSets {
      val f = union(s1, union(s2, s3))
      val g = union(s1, s3)
      assert(exists(f, pos), "Set{1, 2, 3} has at least 1 positive number")
      assert(!exists(f, neg), "Set{1, 2, 3} has no negative number")
      assert(exists(f, even), "Set{1, 2, 3} has at least 1 even number")
      assert(exists(f, odd), "Set{1, 2, 3} has at least 1 odd number")
      assert(exists(g, odd), "Set{1, 3} has at least 1 odd number")
      assert(!exists(g, even), "Set{1, 3} has no even number")
    }
  }
  
  test("Map works properly") {
    new TestSets {
      val f = union(s1, union(s2, s3))
      val plus_1 = map(f, plus)
      val minus_1 = map(f, minus)
      val squared = map(f, square)
      assert(contains(plus_1, 4), "Set{1, 2, 3} + 1 = Set{2, 3, 4}")
      assert(contains(minus_1, 0), "Set{1, 2, 3} - 1 = Set{0, 1, 2} ")
      assert(contains(squared, 4), "Set{1, 2, 3} ** 2 = Set{1, 4, 9}")
      assert(contains(squared, 9), "Set{1, 2, 3} ** 2 = Set{1, 4, 9}")
    }
  }
}
