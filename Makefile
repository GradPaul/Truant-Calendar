# CareerDream Spider Feeder

master:
	@echo "**Building spider-feeder Image..."
	docker build -t "registry.prod.qc.careerdream.com/cd-spider-feeder-service" .
	@echo "**Pushing to Registry server..."
	docker push registry.prod.qc.careerdream.com/cd-spider-feeder-service
	@echo "Done: registry.prod.qc.careerdream.com/cd-spider-feeder-service"

base:
	@echo "**Building spider-feeder base image..."
	docker build -t "registry.prod.qc.careerdream.com/spider-feeder-base-image" ./cmd
	@echo "Done."
