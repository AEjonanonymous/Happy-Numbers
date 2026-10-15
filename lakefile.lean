import Lake
open Lake DSL

package «HappyNumbers» where

require mathlib from git 
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.27.0"

@[default_target]
lean_lib «unified_system_identity_proof» where
  srcDir := "."

lean_lib «basin_density» where
  srcDir := "."

lean_lib «basin_is_bounded» where
  srcDir := "."
