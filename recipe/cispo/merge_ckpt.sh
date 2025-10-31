cd /mnt/shared-storage-user/llmit/user/chengguangran/miniconda3/etc/profile.d
source conda.sh 
conda activate verl
cd /mnt/shared-storage-user/llmit/user/chengguangran/projects/verl-cgr/

python -m verl.model_merger merge \
    --backend fsdp \
    --local_dir /mnt/shared-storage-user/llmit/user/chengguangran/projects/verl-cgr/work_dirs/CISPO/CISPO-Early-Qwen2.5-7B-DAPO-Math/20251029_065251/ckpts/global_step_130/actor \
    --target_dir /mnt/shared-storage-user/llmit/user/chengguangran/projects/verl-cgr/work_dirs/CISPO/CISPO-Early-Qwen2.5-7B-DAPO-Math/20251029_065251/ckpts/global_step_130/actor/huggingface