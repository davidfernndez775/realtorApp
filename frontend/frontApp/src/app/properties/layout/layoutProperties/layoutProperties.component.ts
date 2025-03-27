import { ChangeDetectionStrategy, Component } from '@angular/core';
import { NgbNavModule } from '@ng-bootstrap/ng-bootstrap';
import { SearchFormComponent } from '../../components/searchForm/searchForm.component';
import { MapComponent } from '../../components/map/map.component';
import { ListComponent } from '../../components/list/list.component';

@Component({
  selector: 'app-layout-properties',
  standalone: true,
  imports: [NgbNavModule, SearchFormComponent, MapComponent, ListComponent],
  templateUrl: './layoutProperties.component.html',
  styleUrl: './layoutProperties.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LayoutPropertiesComponent {}
