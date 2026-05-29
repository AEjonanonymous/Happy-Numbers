-- 1. THE CORE ENGINE
def happyStep (n : Nat) : Nat :=
  let digits := (Nat.toDigits 10 n).map (fun c => c.toNat - '0'.toNat)
  digits.foldl (fun acc d => acc + d * d) 0

def isTerminal (n : Nat) : Bool :=
  n ∈ [1, 4, 16, 37, 58, 89, 145, 42, 20]

def digitSum (n : Nat) : Nat :=
  ((Nat.toDigits 10 n).map (fun c => c.toNat - '0'.toNat)).foldl (Nat.add) 0

-- 2. DUAL METRICS (Sum and Length)
def getMetrics : Nat → (Nat × Nat)
| n => 
  let rec loop (val : Nat) (fuel : Nat) (sAcc : Nat) (lAcc : Nat) :=
    if val = 1 then (sAcc + 1, lAcc + 1)
    else if isTerminal val then (sAcc + digitSum val, lAcc + 1)
    else match fuel with
      | 0 => (sAcc, lAcc)
      | f + 1 => loop (happyStep val) f (sAcc + digitSum val) (lAcc + 1)
  loop n 200 0 0

def checkHappy : Nat → Bool
| n => 
  let rec loop (val : Nat) (fuel : Nat) :=
    if val = 1 then true else if isTerminal val then false
    else match fuel with | 0 => false | f + 1 => loop (happyStep val) f
  loop n 200

-- 3. THE DUAL AGGREGATOR
partial def analyzeGoldenDualism (upper : Nat) : (Float × Float) :=
  let rec loop (curr : Nat) (hC hS hL uC uS uL : Nat) :=
    if curr > upper then 
      let rs := (uS.toFloat / uC.toFloat) / (hS.toFloat / hC.toFloat)
      let rl := (uL.toFloat / uC.toFloat) / (hL.toFloat / hC.toFloat)
      (rs, rl)
    else
      let (s, l) := getMetrics curr
      if checkHappy curr then
        loop (curr + 1) (hC + 1) (hS + s) (hL + l) uC uS uL
      else
        loop (curr + 1) hC hS hL (uC + 1) (uS + s) (uL + l)
  loop 1 0 0 0 0 0 0

-- 4. THE EXECUTION
-- This will return (RS, RL). 
-- Watch how they interact to form your Golden Constant.
#eval! analyzeGoldenDualism 1000