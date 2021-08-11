#!/bin/bash
scp $WORKSPACE/docker-compose.yaml ansible@docker-manager
ssh -i ~/.ssh/ansible_id ansible@docker-manager 