import { ChangeDetectionStrategy, Component, TemplateRef } from '@angular/core';
import { NgbModal, NgbModalConfig } from '@ng-bootstrap/ng-bootstrap';
import { FavoriteCardComponent } from '../../components/favoriteCard/favoriteCard.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [FavoriteCardComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
  // add NgbModalConfig and NgbModal to the component providers
  providers: [NgbModalConfig, NgbModal],
})
export class DashboardComponent {
  constructor(config: NgbModalConfig, private modalService: NgbModal) {
    // customize default values of modals used by this component tree
    config.backdrop = 'static';
    config.keyboard = false;
  }

  open(content: TemplateRef<any>) {
    this.modalService.open(content, { size: 'md' });
  }
}
