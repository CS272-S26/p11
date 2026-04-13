dev:
	bundle exec ruby HTTPd.rb

init:
	bundle config set path vendor/bundle
	bundle install

.PHONY: init dev
